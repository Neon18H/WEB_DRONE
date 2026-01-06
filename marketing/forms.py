from django import forms

from marketing.models import Lead


class LeadForm(forms.ModelForm):
    consent = forms.BooleanField(
        required=True,
        label="I agree to be contacted about DRONEX.",
    )

    class Meta:
        model = Lead
        fields = [
            "full_name",
            "organization",
            "work_email",
            "phone",
            "country",
            "sector",
            "use_case",
            "message",
            "consent",
        ]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }
        labels = {
            "full_name": "Full name",
            "organization": "Organization",
            "work_email": "Work email",
            "phone": "Phone (optional)",
            "country": "Country",
            "sector": "Sector",
            "use_case": "Primary use case",
            "message": "Message",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sector"].choices = [
            ("", "Select sector"),
            *self.fields["sector"].choices,
        ]
        self.fields["use_case"].choices = [
            ("", "Select use case"),
            *self.fields["use_case"].choices,
        ]
        for name, field in self.fields.items():
            if name == "consent":
                field.widget.attrs["class"] = "form-check-input"
                continue
            base_class = "form-control dronex-input"
            if isinstance(field.widget, forms.Select):
                base_class = "form-select dronex-input"
            if self.is_bound and name in self.errors:
                base_class = f"{base_class} is-invalid"
            field.widget.attrs["class"] = base_class
            field.widget.attrs.setdefault("placeholder", "")
