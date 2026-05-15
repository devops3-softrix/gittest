# FileForge — Standalone File Converter

42 file conversion tools. Fully self-contained — no installs, no admin rights needed.

---

## How to Use

### First time only
Double-click **`install.bat`**

This will automatically download:
- Python 3.11 embeddable (~10 MB) → saved to `python\`
- FFmpeg static build (~70 MB) → saved to `bin\ffmpeg.exe`
- All Python packages → saved to `python\Lib\site-packages\`

Requires an internet connection. Takes 3–5 minutes.

### Every time after that
Double-click **`start.bat`**

The app starts and your browser opens automatically at `http://127.0.0.1:8000`

---

## Folder Structure After Install

```
FileForge\
├── install.bat         ← run once
├── start.bat           ← run to launch
├── python\             ← embedded Python (auto-downloaded)
├── bin\
│   └── ffmpeg.exe      ← auto-downloaded, used for audio/video
└── FileConverter\      ← Django project
    ├── manage.py
    ├── requirements.txt
    ├── fileconverter\  ← Django config
    └── tools\          ← all 42 conversion tools
```

---

## Conversion Methods

All conversions are 100% pure Python — no LibreOffice, no Word, no system tools:

| Conversion             | Library Used               |
|------------------------|----------------------------|
| PDF → DOCX             | pdf2docx                   |
| PDF → images/SVG       | pymupdf (fitz)             |
| PDF split/merge/encrypt| pypdf                      |
| DOCX → PDF             | python-docx + reportlab    |
| DOCX → ODT             | python-docx + odfpy        |
| DOCX → PPTX            | python-docx + python-pptx  |
| DOCX → PNG/JPG         | python-docx + reportlab + pymupdf |
| XLSX → PDF             | openpyxl + reportlab       |
| PPTX → PDF             | python-pptx + reportlab    |
| TXT → PDF              | reportlab                  |
| Image conversions      | Pillow + pillow-heif       |
| Audio conversions      | ffmpeg.exe (bundled)       |
| Video conversions      | ffmpeg.exe (bundled)       |
| CSV/XLSX tools         | pandas + openpyxl          |

---

## Troubleshooting

**install.bat shows "Failed to download"**
→ Check your internet connection and run install.bat again.

**"Python not found" when running start.bat**
→ Run install.bat first.

**Audio/video conversion fails**
→ Make sure `bin\ffmpeg.exe` exists. If not, run install.bat again or
download manually from https://www.gyan.dev/ffmpeg/builds/ and put `ffmpeg.exe` in the `bin\` folder.

**Port 8000 already in use**
→ start.bat automatically tries 8001, 8002.

**To move the folder**
→ Just move the whole FileForge folder wherever you like. Everything is self-contained.
Run start.bat from the new location. No reinstall needed.
