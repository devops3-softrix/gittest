"""Audio conversion tools."""
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


def _audio_convert(request, in_ext, out_ext, mime, title, description, accept, tool_name, ffmpeg_args=None):
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            uploaded = request.FILES["audio_file"]
            with TempDir() as tmp:
                src = tmp / f"input.{in_ext}"
                src.write_bytes(uploaded.read())
                out = tmp / f"output.{out_ext}"
                ffmpeg_convert(str(src), str(out), ffmpeg_args)
                log_conversion(request, tool_name)
                return file_response(out.read_bytes(), mime, f"converted.{out_ext}")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": title,
        "description": description,
        "accept": accept,
        "field_name": "audio_file",
        "icon": "🎵",
        "category_color": "green",
    })


def m4a_to_mp3(request):
    return _audio_convert(
        request, "m4a", "mp3", "audio/mpeg",
        "M4A → MP3", "Convert Apple M4A audio to MP3.",
        ".m4a", "m4a_to_mp3", ["-q:a", "2"],
    )

def mp3_to_wav(request):
    return _audio_convert(
        request, "mp3", "wav", "audio/wav",
        "MP3 → WAV", "Convert MP3 to uncompressed WAV audio.",
        ".mp3", "mp3_to_wav",
    )

def mp3_to_m4r(request):
    """MP3 → M4R (iPhone ringtone, max 30 s)."""
    return _audio_convert(
        request, "mp3", "m4r", "audio/x-m4r",
        "MP3 → M4R", "Convert MP3 to iPhone ringtone format (M4R, 30 s max).",
        ".mp3", "mp3_to_m4r", ["-t", "30", "-c:a", "aac", "-b:a", "128k", "-f", "ipod"],
    )

def mp4_to_mp3(request):
    return _audio_convert(
        request, "mp4", "mp3", "audio/mpeg",
        "MP4 → MP3", "Extract the audio track from an MP4 video as MP3.",
        ".mp4", "mp4_to_mp3", ["-vn", "-q:a", "2"],
    )

def mp4_to_wav(request):
    return _audio_convert(
        request, "mp4", "wav", "audio/wav",
        "MP4 → WAV", "Extract the audio track from an MP4 video as WAV.",
        ".mp4", "mp4_to_wav", ["-vn"],
    )
