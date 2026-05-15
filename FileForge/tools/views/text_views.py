"""Text and PPTX conversion tools – fully pure Python."""
import json
from io import BytesIO

from django.shortcuts import render
from tools.utils import file_response, pptx_to_pdf_bytes
from tools.conversion_limit import check_conversion_limit, log_conversion


def _check_limit(request):
    allowed, remaining = check_conversion_limit(request)
    if not allowed:
        return render(request, "tools/error.html", {
            "error": "You have used all 3 free conversions. Please sign up for unlimited access."
        })
    return None


def txt_to_pdf(request):
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.units import cm
            from reportlab.lib.styles import ParagraphStyle
            from reportlab.platypus import SimpleDocTemplate, Paragraph

            uploaded = request.FILES["text_file"]
            text = uploaded.read().decode("utf-8", errors="replace")

            buf = BytesIO()
            doc = SimpleDocTemplate(buf, pagesize=A4,
                                    leftMargin=2*cm, rightMargin=2*cm,
                                    topMargin=2*cm, bottomMargin=2*cm)
            style = ParagraphStyle("mono", fontName="Courier", fontSize=10,
                                   leading=14, wordWrap="CJK")
            story = []
            for line in text.splitlines():
                safe = line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
                story.append(Paragraph(safe or "&nbsp;", style))
            doc.build(story)
            buf.seek(0)
            log_conversion(request, "txt_to_pdf")
            return file_response(buf.read(), "application/pdf", "converted.pdf")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": "TXT → PDF",
        "description": "Convert a plain text file to a formatted PDF document.",
        "accept": ".txt",
        "field_name": "text_file",
        "icon": "📄",
        "category_color": "yellow",
    })


def txt_to_json(request):
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            uploaded = request.FILES["text_file"]
            text = uploaded.read().decode("utf-8", errors="replace")
            lines = text.splitlines()
            payload = {"lines": lines, "line_count": len(lines), "content": text}
            data = json.dumps(payload, ensure_ascii=False, indent=2)
            log_conversion(request, "txt_to_json")
            return file_response(data.encode("utf-8"), "application/json", "converted.json")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": "TXT → JSON",
        "description": "Wrap a text file's content in a structured JSON object.",
        "accept": ".txt",
        "field_name": "text_file",
        "icon": "📋",
        "category_color": "yellow",
    })


def pptx_to_pdf(request):
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            uploaded = request.FILES["pptx_file"]
            data = pptx_to_pdf_bytes(uploaded)
            log_conversion(request, "pptx_to_pdf")
            return file_response(data, "application/pdf", "converted.pdf")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": "PPTX → PDF",
        "description": "Convert a PowerPoint presentation to PDF.",
        "accept": ".pptx,.ppt",
        "field_name": "pptx_file",
        "icon": "📊",
        "category_color": "yellow",
    })
