"""Excel and CSV conversion tools."""
from io import BytesIO, StringIO

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


def csv_to_xlsx(request):
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            import pandas as pd
            uploaded = request.FILES["csv_file"]
            df = pd.read_csv(uploaded)
            buf = BytesIO()
            with pd.ExcelWriter(buf, engine="xlsxwriter") as writer:
                df.to_excel(writer, index=False)
            buf.seek(0)
            log_conversion(request, "csv_to_xlsx")
            return file_response(
                buf.read(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "converted.xlsx",
            )
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": "CSV → XLSX",
        "description": "Convert a CSV file to an Excel spreadsheet.",
        "accept": ".csv",
        "field_name": "csv_file",
        "icon": "📊",
        "category_color": "teal",
    })


def csv_to_html(request):
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            import pandas as pd
            uploaded = request.FILES["csv_file"]
            df = pd.read_csv(uploaded)
            html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #ddd;padding:8px;text-align:left}}
th{{background:#f4f4f4}}</style></head>
<body>{df.to_html(index=False)}</body></html>"""
            log_conversion(request, "csv_to_html")
            return file_response(html.encode("utf-8"), "text/html", "table.html")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": "CSV → HTML",
        "description": "Convert a CSV file to an HTML table.",
        "accept": ".csv",
        "field_name": "csv_file",
        "icon": "🌐",
        "category_color": "teal",
    })


def xlsx_to_csv(request):
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            import pandas as pd
            uploaded = request.FILES["xlsx_file"]
            df = pd.read_excel(uploaded)
            buf = StringIO()
            df.to_csv(buf, index=False)
            log_conversion(request, "xlsx_to_csv")
            return file_response(buf.getvalue().encode("utf-8"), "text/csv", "converted.csv")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": "XLSX → CSV",
        "description": "Convert an Excel spreadsheet to CSV format.",
        "accept": ".xlsx,.xls",
        "field_name": "xlsx_file",
        "icon": "📋",
        "category_color": "teal",
    })


def xlsx_to_html(request):
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            import pandas as pd
            uploaded = request.FILES["xlsx_file"]
            df = pd.read_excel(uploaded)
            html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #ddd;padding:8px;text-align:left}}
th{{background:#f4f4f4}}</style></head>
<body>{df.to_html(index=False)}</body></html>"""
            log_conversion(request, "xlsx_to_html")
            return file_response(html.encode("utf-8"), "text/html", "table.html")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": "XLSX → HTML",
        "description": "Convert an Excel spreadsheet to an HTML table.",
        "accept": ".xlsx,.xls",
        "field_name": "xlsx_file",
        "icon": "🌐",
        "category_color": "teal",
    })


def xlsx_to_pdf(request):
    if request.method == "POST":
        limit_resp = _check_limit(request)
        if limit_resp:
            return limit_resp
        try:
            from tools.utils import xlsx_to_pdf_bytes
            uploaded = request.FILES["xlsx_file"]
            data = xlsx_to_pdf_bytes(uploaded)
            log_conversion(request, "xlsx_to_pdf")
            return file_response(data, "application/pdf", "converted.pdf")
        except Exception as e:
            return render(request, "tools/error.html", {"error": str(e)})
    return render(request, "tools/tool_page.html", {
        "title": "XLSX → PDF",
        "description": "Convert an Excel spreadsheet to a PDF document.",
        "accept": ".xlsx,.xls",
        "field_name": "xlsx_file",
        "icon": "📄",
        "category_color": "teal",
    })
