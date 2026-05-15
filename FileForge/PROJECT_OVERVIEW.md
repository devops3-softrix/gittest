# FileForge Project Documentation

Welcome to the documentation for **FileForge**, a powerful, self-contained file conversion platform. This document explains the project's architecture, flow of action, and implementation details for developers and stakeholders.

---

## 🚀 Project Overview

FileForge is a standalone web application built with **Django** that provides **42 specialized file conversion tools**. It is designed to be completely self-contained, requiring no system-wide installations (like LibreOffice or Microsoft Word) and can run portably on Windows.

### Key Features
- **42 Tools**: Spanning PDF, Word, Images, Audio, Video, Excel, and Text categories.
- **Privacy First**: Files are processed locally and deleted immediately after conversion. No cloud APIs are used.
- **Freemium Model**:
  - **Anonymous Users**: Limited to 3 conversions per session.
  - **Registered Users**: Unlimited conversions.
- **SEO Optimized**: Every tool page includes specialized meta-data, usage guides, and "similar tools" sections to drive organic traffic.
- **Portable Design**: Includes batch scripts for automated installation of an embedded Python environment and FFmpeg.

---

## 🏗️ Architecture & Technology Stack

### Backend: Django (Python)
The core logic is handled by a Django application. It uses a variety of open-source libraries for high-fidelity conversions:

| Category | Primary Libraries Used |
| :--- | :--- |
| **PDF** | `pdf2docx`, `pypdf`, `fitz (PyMuPDF)`, `reportlab` |
| **Office** | `python-docx`, `python-pptx`, `openpyxl`, `odfpy` |
| **Images** | `Pillow`, `pillow-heif` |
| **Media** | `FFmpeg` (static binary), `moviepy` (optional) |
| **Data** | `pandas`, `xlsxwriter` |

### Frontend: Modern Web Interface
- **Vanilla CSS**: A premium, responsive design system.
- **Dynamic Context**: A custom decorator pattern injects SEO data and conversion limits into every page without duplicating logic in views.

---

## 📂 Project Structure

```text
FileForge/
├── install.bat             # One-click installer (downloads Python/FFmpeg)
├── start.bat               # Launches the Django server and browser
├── bin/                    # Contains ffmpeg.exe (after install)
├── python/                 # Embedded Python distribution (after install)
└── FileConverter/          # The Django Project
    ├── manage.py           # Django management script
    ├── db.sqlite3          # Database for users and logs
    ├── fileconverter/      # Project settings and configuration
    ├── tools/              # Core application logic
    │   ├── views/          # Modular views (pdf_views.py, audio_views.py, etc.)
    │   ├── conversion_limit.py # Freemium logic & limit tracking
    │   ├── seo_data.py     # SEO metadata for all 42 tools
    │   ├── urls.py         # URL routing and global context injection
    │   └── utils.py        # Shared helpers (file responses, temp dirs)
    ├── templates/          # HTML templates (Base, Home, Tool pages)
    └── static/             # Assets (CSS, JS, Icons)
```

---

## 🔄 Line of Action (Flow of Work)

### 1. User Interaction Flow
1.  **Discovery**: User arrives via the homepage or an SEO-optimized landing page for a specific tool.
2.  **Validation**: The system checks the user's conversion quota:
    *   **Authenticated**: Unlimited access.
    *   **Guest**: Checked against a 3-conversion limit stored in the database/session.
3.  **Upload**: User selects a file. The UI enforces file type restrictions (e.g., `.pdf` only).
4.  **Processing**:
    *   The file is sent via `POST` to the specific conversion view.
    *   A temporary directory is created for the task.
    *   The Python library (e.g., `fitz` for PDF to Image) processes the file in memory or on disk.
5.  **Delivery**: 
    *   The result is wrapped in a `file_response` (single file) or `zip_response` (multiple files).
    *   The browser triggers an automatic download.
6.  **Cleanup**: The temporary directory is purged, and the conversion is logged.

### 2. Developer Workflow (Adding a New Tool)
To add a tool like "PNG to WebP":
1.  **Define SEO**: Add the tool's name, description, and keywords to `tools/seo_data.py`.
2.  **Create View**: Add a function in `tools/views/image_views.py` using `Pillow`.
3.  **Register URL**: Add the path to `tools/urls.py` and include it in the `IMAGE_TOOLS` list for the homepage display.
4.  **Global Injection**: The `_wrap_render` decorator automatically handles the conversion limits and SEO display on the new page.

---

## 🛡️ Privacy & Security
- **Zero Retention**: FileForge does not store user-uploaded files. They exist only for the duration of the request.
- **Local Processing**: Since it runs on the user's machine (or a private server), data never leaves the controlled environment.
- **Encrypted PDF Support**: Includes tools to split/merge even password-protected documents (if the user provides the password).

---

## 📈 SEO & Growth Strategy
The project uses a **"Content-First"** approach. Every one of the 42 tools has:
- A unique **URL slug** (e.g., `/pdf/to-docx/`).
- **Rich Snippets**: Pre-configured meta descriptions and titles.
- **Usage Guides**: "When to use this tool" and "How it works" sections generated dynamically from `seo_data.py`.
- **Internal Linking**: A "Related Tools" sidebar to keep users on the site (e.g., showing "Merge PDF" when a user is on "Split PDF").

---

*This documentation was automatically generated to provide a clear technical roadmap of the FileForge project.*
