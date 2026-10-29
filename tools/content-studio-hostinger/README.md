# a'mie Content Studio (Hostinger)

A standalone version of the Content Studio for Hostinger (PHP, no database).

Files: `index.html` (UI), `api.php` (login, list, save, export), `.htaccess`.
Not in git, built per deploy: `config.php` (team password hash and export key) and `data/store.php` (the products, behind a PHP guard so the browser can't read it).

- Login: the person's name plus the team password. The name is recorded next to every edit.
- Each save keeps the previous version (`prev`) and an hourly backup in `data/backups/`.
- Two people editing at once: the second save is refused (409) and shows the other person's version.
- `api.php?action=export&key=...` returns everything as JSON. Claude reads it before uploading approved copy to Zid.
- Nothing here touches Zid.
