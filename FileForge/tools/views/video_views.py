"""Video conversion tools."""
from django.shortcuts import render
from tools.utils import TempDir, file_response, ffmpeg_convert
from tools.conversion_limit import check_conversion_limit, log_conversion


def _check_limit(request):
    allowed, remaining = check_conversion_limit(request)
    if not allowed:
        return render(request, "tools/error.html", {
            "error": "You have used all 3 free conversions. Please sign up for unlimited access."
        })
    return None


VIDEO_CODECS = {
    "mov":  (["video/quicktime",        ["-c:v", "libx264", "-c:a", "aac"]]),
    "webm": (["video/webm",             ["-c:v", "libvpx-vp9", "-c:a", "libopus"]]),
    "avi":  (["video/x-msvideo",        ["-c:v", "libx264", "-c:a", "mp3"]]),
    "wmv":  (["video/x-ms-wmv",         ["-c:v", "wmv2",   "-c:a", "wmav2"]]),
    "mkv":  (["video/x-matroska",       ["-c:v", "libx264", "-c:a", "aac"]]),
    "flv":  (["video/x-flv",            ["-c:v", "libx264", "-c:a", "aac"]]),
    "mp4":  (["video/mp4",              ["-c:v", "libx264", "-c:a", "aac"]]),
}


def _video_convert(request, in_exts, out_ext, title, description, accept, tool_name):
    mime, codec_args = VIDEO_CODECS[out_ext]
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            uploaded = request.FILES["video_file"]
            original_name = uploaded.name or f"input.{in_exts[0]}"
            in_ext = original_name.rsplit(".", 1)[-1].lower()
            with TempDir() as tmp:
                src = tmp / f"input.{in_ext}"
                src.write_bytes(uploaded.read())
                out = tmp / f"output.{out_ext}"
                ffmpeg_convert(str(src), str(out), codec_args)
                log_conversion(request, tool_name)
                return file_response(out.read_bytes(), mime, f"converted.{out_ext}")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": title,
        "description": description,
        "accept": accept,
        "field_name": "video_file",
        "icon": "🎬",
        "category_color": "orange",
    })


def mp4_to_mov(request):
    return _video_convert(request, ["mp4"], "mov", "MP4 → MOV",
        "Convert MP4 video to Apple QuickTime MOV format.", ".mp4", "mp4_to_mov")

def mp4_to_webm(request):
    return _video_convert(request, ["mp4"], "webm", "MP4 → WebM",
        "Convert MP4 to open WebM format for the web.", ".mp4", "mp4_to_webm")

def mp4_to_avi(request):
    return _video_convert(request, ["mp4"], "avi", "MP4 → AVI",
        "Convert MP4 to AVI format.", ".mp4", "mp4_to_avi")

def mp4_to_wmv(request):
    return _video_convert(request, ["mp4"], "wmv", "MP4 → WMV",
        "Convert MP4 to Windows Media Video format.", ".mp4", "mp4_to_wmv")

def mp4_to_mkv(request):
    return _video_convert(request, ["mp4"], "mkv", "MP4 → MKV",
        "Convert MP4 to Matroska MKV container format.", ".mp4", "mp4_to_mkv")

def mp4_to_flv(request):
    return _video_convert(request, ["mp4"], "flv", "MP4 → FLV",
        "Convert MP4 to Flash Video format.", ".mp4", "mp4_to_flv")

def any_to_mp4(request):
    return _video_convert(
        request, ["mov", "avi", "wmv", "mkv", "flv", "webm"], "mp4",
        "Video → MP4",
        "Convert any video format to the universally compatible MP4.",
        ".mov,.avi,.wmv,.mkv,.flv,.webm,.m4v", "any_to_mp4",
    )
