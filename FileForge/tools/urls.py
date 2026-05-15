from django.urls import path
from django.shortcuts import render
from . import views
from .views.text_views import pptx_to_pdf
from .views.auth_views import login_view, signup_view, logout_view


# ── Tool catalogue ────────────────────────────────────────────────────────
PDF_TOOLS = [
    ("PDF → DOCX",  "Convert PDF to editable Word doc",           "pdf_to_docx",  "📝"),
    ("PDF → TXT",   "Extract all text from a PDF",                "pdf_to_txt",   "📃"),
    ("PDF → PNG",   "Each page as a PNG image (ZIP)",             "pdf_to_png",   "🖼️"),
    ("PDF → JPG",   "Each page as a JPEG image (ZIP)",            "pdf_to_jpg",   "🖼️"),
    ("PDF → BMP",   "Each page as a BMP image (ZIP)",             "pdf_to_bmp",   "🖼️"),
    ("PDF → TIFF",  "Each page as a TIFF image (ZIP)",            "pdf_to_tiff",  "🖼️"),
    ("PDF → PPM",   "Each page as a PPM image (ZIP)",             "pdf_to_ppm",   "🖼️"),
    ("PDF → SVG",   "Each page as vector SVG (ZIP)",              "pdf_to_svg",   "📐"),
    ("PDF → PPTX",  "Each page becomes a slide",                  "pdf_to_pptx",  "📊"),
    ("PDF → XLSX",  "Extract text into spreadsheet rows",         "pdf_to_xlsx",  "📊"),
    ("PDF → CSV",   "Extract text into CSV rows",                 "pdf_to_csv",   "📋"),
    ("PDF → ODT",   "Convert to OpenDocument Text",               "pdf_to_odt",   "📝"),
    ("PDF → ZIP",   "Wrap a PDF inside a ZIP archive",            "pdf_to_zip",   "🗜️"),
    ("Split PDF",   "Split into individual page PDFs",            "pdf_split",    "✂️"),
    ("Merge PDFs",  "Combine multiple PDFs into one",             "pdf_merge",    "🔗"),
    ("Encrypt PDF", "Password-protect your PDF",                  "pdf_encrypt",  "🔒"),
]

DOCX_TOOLS = [
    ("DOCX → PDF",  "Word doc to PDF",                           "docx_to_pdf",  "📄"),
    ("DOCX → TXT",  "Extract plain text from Word doc",           "docx_to_txt",  "📃"),
    ("DOCX → ODT",  "Word to OpenDocument Text",                  "docx_to_odt",  "📝"),
    ("DOCX → PPTX", "Each Word page becomes a slide",             "docx_to_pptx", "📊"),
    ("DOCX → PNG",  "Each Word page as PNG image (ZIP)",          "docx_to_png",  "🖼️"),
    ("DOCX → JPG",  "Each Word page as JPEG image (ZIP)",         "docx_to_jpg",  "🖼️"),
]

IMAGE_TOOLS = [
    ("Image → JPG",  "Convert any image to JPEG",                 "to_jpg",  "🖼️"),
    ("Image → PNG",  "Convert any image to PNG",                  "to_png",  "🖼️"),
    ("Image → BMP",  "Convert any image to BMP",                  "to_bmp",  "🖼️"),
    ("Image → TIFF", "Convert any image to TIFF",                 "to_tiff", "🖼️"),
    ("Image → WebP", "Convert any image to modern WebP",          "to_webp", "🖼️"),
    ("Image → HEIC", "Convert any image to Apple HEIC",           "to_heic", "🖼️"),
]

AUDIO_TOOLS = [
    ("M4A → MP3",  "Apple M4A audio to MP3",                      "m4a_to_mp3", "🎵"),
    ("MP3 → WAV",  "MP3 to uncompressed WAV",                     "mp3_to_wav", "🎵"),
    ("MP3 → M4R",  "MP3 to iPhone ringtone (30 s max)",           "mp3_to_m4r", "📱"),
    ("MP4 → MP3",  "Extract audio from video as MP3",             "mp4_to_mp3", "🎵"),
    ("MP4 → WAV",  "Extract audio from video as WAV",             "mp4_to_wav", "🎵"),
]

VIDEO_TOOLS = [
    ("MP4 → MOV",   "MP4 to Apple QuickTime MOV",                 "mp4_to_mov",  "🎬"),
    ("MP4 → WebM",  "MP4 to open WebM format",                    "mp4_to_webm", "🎬"),
    ("MP4 → AVI",   "MP4 to AVI format",                          "mp4_to_avi",  "🎬"),
    ("MP4 → WMV",   "MP4 to Windows Media Video",                 "mp4_to_wmv",  "🎬"),
    ("MP4 → MKV",   "MP4 to Matroska container",                  "mp4_to_mkv",  "🎬"),
    ("MP4 → FLV",   "MP4 to Flash Video format",                  "mp4_to_flv",  "🎬"),
    ("Video → MP4", "Any video format to universal MP4",          "any_to_mp4",  "🎬"),
]

EXCEL_TOOLS = [
    ("CSV → XLSX",  "CSV file to Excel spreadsheet",              "csv_to_xlsx",  "📊"),
    ("CSV → HTML",  "CSV data to HTML table",                     "csv_to_html",  "🌐"),
    ("XLSX → CSV",  "Excel spreadsheet to CSV",                   "xlsx_to_csv",  "📋"),
    ("XLSX → HTML", "Excel spreadsheet to HTML table",            "xlsx_to_html", "🌐"),
    ("XLSX → PDF",  "Excel spreadsheet to PDF",                   "xlsx_to_pdf",  "📄"),
]

TEXT_TOOLS = [
    ("TXT → PDF",   "Plain text to formatted PDF",                "txt_to_pdf",   "📄"),
    ("TXT → JSON",  "Wrap text content in JSON structure",        "txt_to_json",  "📋"),
    ("PPTX → PDF",  "PowerPoint presentation to PDF",             "pptx_to_pdf",  "📊"),
]

# Flat list for related-tool lookups
ALL_TOOLS_FLAT = (PDF_TOOLS + DOCX_TOOLS + IMAGE_TOOLS + AUDIO_TOOLS
                  + VIDEO_TOOLS + EXCEL_TOOLS + TEXT_TOOLS)

_INFO_BADGES = [
    {"icon": "🔒", "label": "Files deleted after download"},
    {"icon": "⚡", "label": "Instant conversion"},
    {"icon": "📦", "label": "Max 100 MB"},
]

_NAV_CATEGORIES = [
    ("pdf",    "PDF"),
    ("docx",   "Word"),
    ("images", "Images"),
    ("audio",  "Audio"),
    ("video",  "Video"),
    ("excel",  "Excel"),
    ("text",   "Text"),
]


def _make_tool_list(entries):
    from django.urls import reverse
    return [
        {"name": name, "description": desc, "url": reverse(url_name), "icon": icon}
        for name, desc, url_name, icon in entries
    ]


def home(request):
    ctx = {
        "pdf_tools":   _make_tool_list(PDF_TOOLS),
        "docx_tools":  _make_tool_list(DOCX_TOOLS),
        "image_tools": _make_tool_list(IMAGE_TOOLS),
        "audio_tools": _make_tool_list(AUDIO_TOOLS),
        "video_tools": _make_tool_list(VIDEO_TOOLS),
        "excel_tools": _make_tool_list(EXCEL_TOOLS),
        "text_tools":  _make_tool_list(TEXT_TOOLS),
        "stats": [
            ("42",   "tools"),
            ("7",    "categories"),
            ("100%", "server-side"),
        ],
        "how_it_works": [
            {"step": "01", "icon": "📁", "title": "Upload your file",
             "desc": "Drag and drop or click to browse. Supports files up to 100 MB."},
            {"step": "02", "icon": "⚙️", "title": "We convert it",
             "desc": "Your file is processed instantly using modern Python libraries — no cloud services."},
            {"step": "03", "icon": "⬇️", "title": "Download the result",
             "desc": "Your converted file starts downloading immediately. Nothing is stored on our servers."},
        ],
        "nav_categories": _NAV_CATEGORIES,
    }
    return render(request, "home.html", ctx)


# ── Inject nav + badge + SEO + limit context into every tool view ─────────

def _wrap_render(original_render):
    def patched(request, template, ctx=None, **kwargs):
        ctx = ctx or {}
        ctx.setdefault("nav_categories", _NAV_CATEGORIES)
        if template == "tools/tool_page.html":
            ctx.setdefault("info_badges", _INFO_BADGES)

            # ── Conversion limit info ─────────────────────────────
            from .conversion_limit import check_conversion_limit
            allowed, remaining = check_conversion_limit(request)
            ctx.setdefault("limit_reached", not allowed)
            ctx.setdefault("conversions_remaining", remaining)
            ctx.setdefault("is_authenticated", request.user.is_authenticated)

            # ── SEO + related tools ───────────────────────────────
            url_name = None
            if hasattr(request, "resolver_match") and request.resolver_match:
                url_name = request.resolver_match.url_name
            if url_name:
                from .seo_data import get_seo_data, get_related_tools
                seo = get_seo_data(url_name)
                if seo:
                    ctx.setdefault("seo_title", seo.get("seo_title", ""))
                    ctx.setdefault("seo_description", seo.get("seo_description", ""))
                    ctx.setdefault("long_description", seo.get("long_description", ""))
                    ctx.setdefault("use_cases", seo.get("use_cases", []))
                related = get_related_tools(url_name, ALL_TOOLS_FLAT)
                ctx.setdefault("related_tools", related)

        return original_render(request, template, ctx, **kwargs)
    return patched


import tools.views.pdf_views   as _pv
import tools.views.docx_views  as _dv
import tools.views.image_views as _iv
import tools.views.audio_views as _av
import tools.views.video_views as _vv
import tools.views.excel_views as _ev
import tools.views.text_views  as _tv

from django.shortcuts import render as _base_render

for _mod in (_pv, _dv, _iv, _av, _vv, _ev, _tv):
    _mod.render = _wrap_render(_base_render)  # type: ignore


# ── URL patterns ──────────────────────────────────────────────────────────

urlpatterns = [
    path("", home, name="home"),

    # Auth
    path("login/",  login_view,  name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),

    # PDF
    path("pdf/to-docx/",    views.pdf_to_docx,  name="pdf_to_docx"),
    path("pdf/to-txt/",     views.pdf_to_txt,   name="pdf_to_txt"),
    path("pdf/to-png/",     views.pdf_to_png,   name="pdf_to_png"),
    path("pdf/to-jpg/",     views.pdf_to_jpg,   name="pdf_to_jpg"),
    path("pdf/to-bmp/",     views.pdf_to_bmp,   name="pdf_to_bmp"),
    path("pdf/to-tiff/",    views.pdf_to_tiff,  name="pdf_to_tiff"),
    path("pdf/to-ppm/",     views.pdf_to_ppm,   name="pdf_to_ppm"),
    path("pdf/to-svg/",     views.pdf_to_svg,   name="pdf_to_svg"),
    path("pdf/to-pptx/",    views.pdf_to_pptx,  name="pdf_to_pptx"),
    path("pdf/to-xlsx/",    views.pdf_to_xlsx,   name="pdf_to_xlsx"),
    path("pdf/to-csv/",     views.pdf_to_csv,   name="pdf_to_csv"),
    path("pdf/to-odt/",     views.pdf_to_odt,   name="pdf_to_odt"),
    path("pdf/to-zip/",     views.pdf_to_zip,   name="pdf_to_zip"),
    path("pdf/split/",      views.pdf_split,    name="pdf_split"),
    path("pdf/merge/",      views.pdf_merge,    name="pdf_merge"),
    path("pdf/encrypt/",    views.pdf_encrypt,  name="pdf_encrypt"),

    # DOCX
    path("docx/to-pdf/",    views.docx_to_pdf,  name="docx_to_pdf"),
    path("docx/to-txt/",    views.docx_to_txt,  name="docx_to_txt"),
    path("docx/to-odt/",    views.docx_to_odt,  name="docx_to_odt"),
    path("docx/to-pptx/",   views.docx_to_pptx, name="docx_to_pptx"),
    path("docx/to-png/",    views.docx_to_png,  name="docx_to_png"),
    path("docx/to-jpg/",    views.docx_to_jpg,  name="docx_to_jpg"),

    # Images
    path("image/to-jpg/",   views.to_jpg,   name="to_jpg"),
    path("image/to-png/",   views.to_png,   name="to_png"),
    path("image/to-bmp/",   views.to_bmp,   name="to_bmp"),
    path("image/to-tiff/",  views.to_tiff,  name="to_tiff"),
    path("image/to-webp/",  views.to_webp,  name="to_webp"),
    path("image/to-heic/",  views.to_heic,  name="to_heic"),

    # Audio
    path("audio/m4a-to-mp3/", views.m4a_to_mp3, name="m4a_to_mp3"),
    path("audio/mp3-to-wav/", views.mp3_to_wav,  name="mp3_to_wav"),
    path("audio/mp3-to-m4r/", views.mp3_to_m4r,  name="mp3_to_m4r"),
    path("audio/mp4-to-mp3/", views.mp4_to_mp3,  name="mp4_to_mp3"),
    path("audio/mp4-to-wav/", views.mp4_to_wav,  name="mp4_to_wav"),

    # Video
    path("video/mp4-to-mov/",   views.mp4_to_mov,  name="mp4_to_mov"),
    path("video/mp4-to-webm/",  views.mp4_to_webm, name="mp4_to_webm"),
    path("video/mp4-to-avi/",   views.mp4_to_avi,  name="mp4_to_avi"),
    path("video/mp4-to-wmv/",   views.mp4_to_wmv,  name="mp4_to_wmv"),
    path("video/mp4-to-mkv/",   views.mp4_to_mkv,  name="mp4_to_mkv"),
    path("video/mp4-to-flv/",   views.mp4_to_flv,  name="mp4_to_flv"),
    path("video/to-mp4/",       views.any_to_mp4,  name="any_to_mp4"),

    # Excel / CSV
    path("excel/csv-to-xlsx/",  views.csv_to_xlsx,  name="csv_to_xlsx"),
    path("excel/csv-to-html/",  views.csv_to_html,  name="csv_to_html"),
    path("excel/xlsx-to-csv/",  views.xlsx_to_csv,  name="xlsx_to_csv"),
    path("excel/xlsx-to-html/", views.xlsx_to_html, name="xlsx_to_html"),
    path("excel/xlsx-to-pdf/",  views.xlsx_to_pdf,  name="xlsx_to_pdf"),

    # Text / PPTX
    path("text/to-pdf/",   views.txt_to_pdf,  name="txt_to_pdf"),
    path("text/to-json/",  views.txt_to_json, name="txt_to_json"),
    path("pptx/to-pdf/",   pptx_to_pdf,       name="pptx_to_pdf"),
]
