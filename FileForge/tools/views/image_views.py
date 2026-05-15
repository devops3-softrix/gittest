"""Image conversion tools."""
from io import BytesIO

from django.shortcuts import render

from tools.utils import file_response
from tools.conversion_limit import check_conversion_limit, log_conversion


def _check_limit(request):
    allowed, remaining = check_conversion_limit(request)
    if not allowed:
        return render(request, "tools/error.html", {
            "error": "You have used all 3 free conversions. Please sign up for unlimited access."
        })
    return None


FORMATS = {
    "jpg":  ("JPEG",  "image/jpeg",  ".jpg,.jpeg,.png,.bmp,.tiff,.webp,.heic,.heif"),
    "png":  ("PNG",   "image/png",   ".jpg,.jpeg,.png,.bmp,.tiff,.webp,.heic,.heif"),
    "bmp":  ("BMP",   "image/bmp",   ".jpg,.jpeg,.png,.bmp,.tiff,.webp"),
    "tiff": ("TIFF",  "image/tiff",  ".jpg,.jpeg,.png,.bmp,.tiff,.webp"),
    "webp": ("WEBP",  "image/webp",  ".jpg,.jpeg,.png,.bmp,.tiff,.webp,.heic,.heif"),
    "heic": ("HEIF",  "image/heic",  ".jpg,.jpeg,.png,.bmp,.tiff,.webp"),
}


def _convert(request, fmt, title, description):
    pil_fmt, mime, accept = FORMATS[fmt]
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            from PIL import Image
            try:
                from pillow_heif import register_heif_opener
                register_heif_opener()
            except ImportError:
                pass
            uploaded = request.FILES["image_file"]
            img = Image.open(uploaded)
            if img.mode not in ("RGB", "RGBA") and pil_fmt not in ("PNG", "TIFF"):
                img = img.convert("RGB")
            buf = BytesIO()
            img.save(buf, pil_fmt)
            buf.seek(0)
            log_conversion(request, f"to_{fmt}")
            return file_response(buf.read(), mime, f"converted.{fmt}")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": title,
        "description": description,
        "accept": accept,
        "field_name": "image_file",
        "icon": "🖼️",
        "category_color": "purple",
    })


def to_jpg(request):
    return _convert(request, "jpg", "Image → JPG", "Convert any image to JPEG format.")

def to_png(request):
    return _convert(request, "png", "Image → PNG", "Convert any image to PNG format.")

def to_bmp(request):
    return _convert(request, "bmp", "Image → BMP", "Convert any image to BMP format.")

def to_tiff(request):
    return _convert(request, "tiff", "Image → TIFF", "Convert any image to TIFF format.")

def to_webp(request):
    return _convert(request, "webp", "Image → WebP", "Convert any image to modern WebP format.")

def to_heic(request):
    return _convert(request, "heic", "Image → HEIC", "Convert any image to Apple HEIC format.")
