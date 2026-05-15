# FileForge — Standalone File Converter

42 file conversion tools. Fully self-contained — no installs, no admin rights needed.

---

## Overview

FileForge is a Django-based web application serving 42 file conversion tools, deployed on a Linux server using a LEMP stack (Linux, Nginx, MySQL/SQLite, Python/Gunicorn). The app is served from the `/fileforge` subpath and uses Tailwind CSS v4.

---

## Conversion Methods

All conversions are 100% pure Python — no LibreOffice, no Word, no system tools:

| Conversion              | Library Used                      |
| ----------------------- | --------------------------------- |
| PDF → DOCX              | pdf2docx                          |
| PDF → images/SVG        | pymupdf (fitz)                    |
| PDF split/merge/encrypt | pypdf                             |
| DOCX → PDF              | python-docx + reportlab           |
| DOCX → ODT              | python-docx + odfpy               |
| DOCX → PPTX             | python-docx + python-pptx         |
| DOCX → PNG/JPG          | python-docx + reportlab + pymupdf |
| XLSX → PDF              | openpyxl + reportlab              |
| PPTX → PDF              | python-pptx + reportlab           |
| TXT → PDF               | reportlab                         |
| Image conversions       | Pillow + pillow-heif              |
| Audio conversions       | ffmpeg (system)                   |
| Video conversions       | ffmpeg (system)                   |
| CSV/XLSX tools          | pandas + openpyxl                 |

---

## Folder Structure

```
FileForge/
├── python/             ← virtual environment
├── bin/                ← (legacy; ffmpeg now installed system-wide)
└── FileConverter/      ← Django project
    ├── manage.py
    ├── requirements.txt
    ├── fileconverter/  ← Django config (settings.py, wsgi.py, urls.py)
    └── tools/          ← all 42 conversion tools
```

---

## Deployment Guide (Linux / LEMP)

### 1. System Requirements & Dependencies

Install the necessary system packages, including FFmpeg for media conversions and the Python environment:

```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx ffmpeg libmagic1 -y
```

---

### 2. Project Initialization

Navigate to the project root and set up the virtual environment:

```bash
cd /var/www/FileForge
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn python-dotenv
```

---

### 3. Django Configuration (`settings.py`)

Modify `/var/www/FileForge/fileconverter/settings.py` to handle the subpath and security:

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['10.0.2.11', 'localhost', '127.0.0.1']

# Subpath Configuration
FORCE_SCRIPT_NAME = '/fileforge'
STATIC_URL = '/fileforge/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')

MEDIA_URL = '/fileforge/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
```

---

### 4. Tailwind CSS v4 Setup

FileForge uses the Tailwind CSS v4 standalone CLI (no Node.js or `tailwind.config.js` required).

**Download the CLI:**

```bash
cd /var/www/FileForge
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
chmod +x tailwindcss-linux-x64
mv tailwindcss-linux-x64 tailwindcss
```

**Create the input CSS file at `static/input.css`:**

```css
@import "tailwindcss";

/* Scan HTML templates for classes */
@source "../templates/**/*.html";
@source "../tools/templates/**/*.html";

@theme {
  --color-surface: #0f1117;
  --color-panel: #161b27;
  --color-border: #1f2937;
  --color-muted: #6b7280;
  --color-accent: #6366f1;

  --font-display: "Syne", sans-serif;
  --font-body: "Outfit", sans-serif;
}
```

**Build and collect static files:**

```bash
# Compile CSS
./tailwindcss -i ./static/input.css -o ./static/output.css --minify

# Sync with Django
python manage.py collectstatic --noinput
```

---

### 5. Gunicorn Service Configuration

Create `/etc/systemd/system/gunicorn.service`:

```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
Environment="DJANGO_SECRET_KEY=your_secret_key_here"
WorkingDirectory=/var/www/FileForge
ExecStart=/var/www/FileForge/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          fileconverter.wsgi:application

[Install]
WantedBy=multi-user.target
```

---

### 6. Nginx Configuration

Add the following blocks to your existing `/etc/nginx/sites-available/default` server block (merges cleanly with any existing PHP configuration):

```nginx
# --- FILEFORGE (DJANGO) ---
location /fileforge/static/ {
    alias /var/www/FileForge/static_root/;
}

location /fileforge/media/ {
    alias /var/www/FileForge/media/;
}

location /fileforge/ {
    include proxy_params;
    proxy_pass http://unix:/run/gunicorn.sock;
    proxy_set_header SCRIPT_NAME /fileforge;
}
```

---

### 7. Frontend Template Fixes (`base.html`)

Update your base template to respect the subpath:

1. **Load static files** — add at the top of the template:
   ```html
   {% load static %}
   ```

2. **Replace the Tailwind CDN script** with the compiled stylesheet:
   ```html
   <link rel="stylesheet" href="{% static 'output.css' %}">
   ```

3. **Update hardcoded navbar URLs:**
   - `href="/"` → `href="/fileforge/"`
   - `href="/#{{ cat }}"` → `href="/fileforge/#{{ cat }}"`
   - Update `login`, `logout`, and `signup` paths similarly.

---

### 8. Permissions & Service Startup

Ensure the web server owns the project files, then start all services:

```bash
sudo chown -R www-data:www-data /var/www/FileForge
sudo chmod -R 755 /var/www/FileForge
sudo chmod 664 /var/www/FileForge/db.sqlite3

sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

---

## Troubleshooting

**`pip install` fails**
→ Make sure the virtual environment is activated: `source venv/bin/activate`

**Audio/video conversion fails**
→ Confirm ffmpeg is installed: `ffmpeg -version`. If missing, re-run: `sudo apt install ffmpeg -y`

**Static files not loading (404)**
→ Re-run `python manage.py collectstatic --noinput` and verify the `alias` paths in Nginx match `STATIC_ROOT`.

**Port/socket conflicts**
→ Check Gunicorn status: `sudo systemctl status gunicorn`. Review logs: `sudo journalctl -u gunicorn`

**"DisallowedHost" Django error**
→ Add your server's IP or domain to `ALLOWED_HOSTS` in `settings.py`.

**To move the project directory**
→ Move the entire `/var/www/FileForge` folder, update all paths in `gunicorn.service` and the Nginx config, then restart both services. No reinstall needed.