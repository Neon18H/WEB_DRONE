from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST

from marketing.forms import LeadForm


@require_GET
def landing(request: HttpRequest) -> HttpResponse:
    form = LeadForm()
    return render(request, "marketing/landing.html", {"form": form})


@require_POST
def contact_submit(request: HttpRequest) -> HttpResponse:
    form = LeadForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(
            request,
            "Request received. Our team will follow up shortly.",
        )
        return redirect(reverse("marketing:thank_you"))
    messages.error(request, "Please review the highlighted fields.")
    return render(request, "marketing/landing.html", {"form": form})


@require_GET
def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request, "marketing/thank_you.html")
