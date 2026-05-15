"""
Conversion usage tracking and free-tier limit enforcement.

Anonymous users get FREE_CONVERSION_LIMIT conversions per session.
Authenticated users get unlimited conversions.
"""
from .models import ConversionLog

FREE_CONVERSION_LIMIT = 3


def _ensure_session(request):
    """Make sure a session key exists (even for anonymous users)."""
    if not request.session.session_key:
        request.session.create()


def get_conversion_count(request):
    """Return the number of conversions this session has performed."""
    _ensure_session(request)
    return ConversionLog.objects.filter(
        session_key=request.session.session_key
    ).count()


def check_conversion_limit(request):
    """
    Returns (allowed: bool, remaining: int).
    Authenticated users always get (True, -1) meaning unlimited.
    """
    if request.user.is_authenticated:
        return True, -1  # unlimited

    count = get_conversion_count(request)
    remaining = max(0, FREE_CONVERSION_LIMIT - count)
    allowed = remaining > 0
    return allowed, remaining


def log_conversion(request, tool_name):
    """Record a successful conversion."""
    _ensure_session(request)
    ConversionLog.objects.create(
        session_key=request.session.session_key,
        user=request.user if request.user.is_authenticated else None,
        tool_name=tool_name,
    )
