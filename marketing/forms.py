from django import forms

from marketing.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            "name",
            "org",
            "email",
            "phone",
            "country",
            "use_case",
            "message",
        ]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            base_class = "form-control dronex-input"
            field.widget.attrs["class"] = base_class
            field.widget.attrs.setdefault("placeholder", "")
