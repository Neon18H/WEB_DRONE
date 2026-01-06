from django.contrib import admin

from marketing.models import Lead, LeadSource, NewsletterSignup


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "organization",
        "work_email",
        "sector",
        "use_case",
        "created_at",
    )
    list_filter = ("sector", "use_case", "created_at")
    search_fields = ("full_name", "organization", "work_email")
    readonly_fields = ("created_at",)


@admin.register(LeadSource)
class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ("email", "organization", "created_at")
    search_fields = ("email", "organization")
    readonly_fields = ("created_at",)
