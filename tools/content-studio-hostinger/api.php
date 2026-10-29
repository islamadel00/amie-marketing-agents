<?php
require __DIR__ . '/config.php';
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
session_set_cookie_params(['lifetime' => 60 * 60 * 24 * 30, 'httponly' => true, 'samesite' => 'Lax', 'secure' => !empty($_SERVER['HTTPS'])]);
session_start();

function out($data, $code = 200) { http_response_code($code); echo json_encode($data, JSON_UNESCAPED_UNICODE); exit; }
const GUARD = "<?php http_response_code(404); exit; ?>\n";
function decode_store($raw) {
  if (strncmp($raw, GUARD, strlen(GUARD)) === 0) $raw = substr($raw, strlen(GUARD));
  return json_decode($raw ?: '{}', true) ?: [];
}
function load() { return decode_store((string)@file_get_contents(DATA_FILE)); }
function public_rows($all) {
  $rows = [];
  foreach ($all as $id => $r) { $r['id'] = $id; $rows[] = $r; }
  usort($rows, fn($a, $b) => ($a['order'] ?? 999) <=> ($b['order'] ?? 999));
  return $rows;
}

$action = $_GET['action'] ?? '';
$body = json_decode(file_get_contents('php://input') ?: '{}', true) ?: [];

if ($action === 'login') {
  $name = trim((string)($body['name'] ?? ''));
  $pass = (string)($body['password'] ?? '');
  if ($name === '' || mb_strlen($name) > 40) out(['error' => 'name'], 400);
  if (!hash_equals(TEAM_PASS_SHA256, hash('sha256', $pass))) { usleep(600000); out(['error' => 'password'], 401); }
  session_regenerate_id(true);
  $_SESSION['name'] = $name;
  out(['ok' => true, 'name' => $name]);
}
if ($action === 'logout') { $_SESSION = []; session_destroy(); out(['ok' => true]); }

if ($action === 'export') {
  if (!hash_equals(EXPORT_KEY, (string)($_GET['key'] ?? ''))) out(['error' => 'key'], 403);
  out(['rows' => public_rows(load())]);
}

if (empty($_SESSION['name'])) out(['error' => 'auth'], 401);

if ($action === 'me') out(['name' => $_SESSION['name']]);

if ($action === 'list') {
  $all = load();
  $stamp = 0;
  foreach ($all as $r) $stamp = max($stamp, strtotime($r['updatedAt'] ?? '') ?: 0);
  out(['rows' => public_rows($all), 'stamp' => $stamp]);
}

if ($action === 'save' && $_SERVER['REQUEST_METHOD'] === 'POST') {
  $id = (string)($body['id'] ?? '');
  $fields = ['short_new', 'long_new', 'notes', 'status'];
  $statuses = ['draft', 'review', 'approved', 'live'];
  $fh = fopen(DATA_FILE, 'c+');
  if (!$fh || !flock($fh, LOCK_EX)) out(['error' => 'busy'], 503);
  $all = decode_store((string)stream_get_contents($fh));
  if (!isset($all[$id])) { flock($fh, LOCK_UN); out(['error' => 'missing'], 404); }
  $r = $all[$id];
  if ((int)($body['v'] ?? 0) !== (int)($r['v'] ?? 1)) { flock($fh, LOCK_UN); out(['error' => 'conflict', 'row' => $r + ['id' => $id]], 409); }
  if (isset($body['status']) && !in_array($body['status'], $statuses, true)) { flock($fh, LOCK_UN); out(['error' => 'status'], 400); }
  $r['prev'] = ['short_new' => $r['short_new'] ?? '', 'long_new' => $r['long_new'] ?? '', 'status' => $r['status'] ?? 'draft', 'updatedAt' => $r['updatedAt'] ?? '', 'updatedBy' => $r['updatedBy'] ?? ''];
  foreach ($fields as $f) if (isset($body[$f]) && is_string($body[$f])) $r[$f] = mb_substr($body[$f], 0, 20000);
  $r['updatedAt'] = gmdate('c');
  $r['updatedBy'] = $_SESSION['name'];
  $r['v'] = (int)($r['v'] ?? 1) + 1;
  $all[$id] = $r;
  if (!is_dir(BACKUP_DIR)) @mkdir(BACKUP_DIR, 0750, true);
  @copy(DATA_FILE, BACKUP_DIR . '/store-' . gmdate('Ymd-H') . '.php');
  ftruncate($fh, 0); rewind($fh);
  fwrite($fh, GUARD . json_encode($all, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
  fflush($fh); flock($fh, LOCK_UN); fclose($fh);
  out(['ok' => true, 'row' => $r + ['id' => $id]]);
}

out(['error' => 'action'], 400);
