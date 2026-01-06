from django.db import models


class LeadSource(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Lead(models.Model):
    SECTOR_CHOICES = [
        ("law_enforcement", "Law Enforcement"),
        ("private_security", "Private Security"),
        ("critical_infra", "Critical Infrastructure"),
        ("government", "Government / Defense"),
        ("smart_city", "Smart City / Traffic"),
        ("emergency_response", "Emergency Response"),
        ("industrial", "Industrial Operations"),
        ("other", "Other"),
    ]
    USE_CASE_CHOICES = [
        ("incident_response", "Incident response"),
        ("perimeter_security", "Perimeter security"),
        ("crowd_monitoring", "Crowd monitoring"),
        ("critical_asset", "Critical asset monitoring"),
        ("search_rescue", "Search & rescue"),
        ("traffic", "Traffic & mobility"),
        ("inspection", "Infrastructure inspection"),
        ("other", "Other"),
    ]

    full_name = models.CharField(max_length=140)
    organization = models.CharField(max_length=180)
    work_email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=80)
    sector = models.CharField(max_length=40, choices=SECTOR_CHOICES)
    use_case = models.CharField(max_length=40, choices=USE_CASE_CHOICES)
    message = models.TextField(blank=True)
    consent = models.BooleanField(default=False)
    source = models.ForeignKey(
        LeadSource,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.full_name} · {self.organization}"


class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True)
    organization = models.CharField(max_length=180, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.email
