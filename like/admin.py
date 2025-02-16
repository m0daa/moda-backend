from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "curation", "created_at")
    search_fields = ("user__username", "curation__title")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
