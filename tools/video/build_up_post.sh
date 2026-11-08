#!/usr/bin/env bash
# Glow Friday "build-up" post: reverse the AI disassembly clip(s), hold the final (real) frame,
# then hand off into the local hero loop. Usage:
#   tools/video/build_up_post.sh out.mp4 clip1.mp4 [clip2.mp4]
# With two clips (A: ribbon-off, then boxes-out) pass them in GENERATION order; they are
# reversed and played boxes-in first, ribbon-on last.
set -euo pipefail
OUT="$1"; shift
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
HERO="$ROOT/content/campaigns/2026-11-glow-friday/hero/glow-friday-hero-mobile-9x16-notext.mp4"
TMP="$(mktemp -d)"
n=0
for c in "$@"; do
  n=$((n+1))
  ffmpeg -loglevel error -y -i "$c" -an -vf "reverse,scale=1080:1920:flags=lanczos,fps=30,format=yuv420p" "$TMP/r$n.mp4"
done
# play order: last generated clip first (reversed)
LIST="$TMP/list.txt"; : > "$LIST"
for ((i=n; i>=1; i--)); do echo "file '$TMP/r$i.mp4'" >> "$LIST"; done
ffmpeg -loglevel error -y -f concat -safe 0 -i "$LIST" -c copy "$TMP/build.mp4"
# 1 s hold on the final frame (the real photo), then 3 s of the existing hero loop
ffmpeg -loglevel error -y -i "$TMP/build.mp4" -vf "tpad=stop_mode=clone:stop_duration=1" -an "$TMP/hold.mp4"
ffmpeg -loglevel error -y -i "$TMP/hold.mp4" -t 3 -i "$HERO" -filter_complex \
 "[0:v]fps=30,format=yuv420p[a];[1:v]fps=30,format=yuv420p,trim=0:3,setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1[v]" \
 -map "[v]" -c:v libx264 -crf 20 -preset slow -movflags +faststart "$OUT"
echo "done $OUT"; rm -rf "$TMP"
