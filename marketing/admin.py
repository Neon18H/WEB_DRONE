from django.contrib import admin

from marketing.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "org", "email", "phone", "country", "created_at")
    list_filter = ("country", "created_at")
    search_fields = ("name", "org", "email")
