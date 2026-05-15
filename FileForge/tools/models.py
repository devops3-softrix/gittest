"""Models for the tools app — tracks conversion usage for rate limiting."""
from django.conf import settings
from django.db import models


class ConversionLog(models.Model):
    """Records each conversion to enforce free-tier limits for anonymous users."""
    session_key = models.CharField(max_length=40, db_index=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="conversions",
    )
    tool_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        who = self.user.username if self.user else f"anon:{self.session_key[:8]}"
        return f"{who} — {self.tool_name} @ {self.created_at:%Y-%m-%d %H:%M}"
