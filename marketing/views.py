from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST

from marketing.forms import LeadForm

BENEFITS = [
    "Centro de mando unificado multi-dron",
    "Operación por turnos y rutas (zonas geo + waypoints)",
    "Alertas tácticas (pilot→admin, pilot→pilot)",
    "Telemetría en tiempo real + estado del enlace",
    "Control de operación (start/end) + bitácora",
    "Auditoría completa (quién hizo qué y cuándo)",
    "Escalabilidad (de 5 a 500 drones)",
    "Integración con drones comerciales o propios (agente)",
    "Evidencia y reportabilidad",
    "Permisos por rol y segregación de funciones",
]


@require_GET
def landing_view(request: HttpRequest) -> HttpResponse:
    form = LeadForm()
    return render(
        request,
        "marketing/landing.html",
        {"form": form, "benefits": BENEFITS},
    )


@require_POST
def contact_submit(request: HttpRequest) -> HttpResponse:
    form = LeadForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(
            request,
            "Solicitud recibida. Nuestro equipo se pondrá en contacto pronto.",
        )
    else:
        messages.error(
            request,
            "Revisa los campos marcados e intenta nuevamente.",
        )
        return render(
            request,
            "marketing/landing.html",
            {"form": form, "benefits": BENEFITS},
        )
    return redirect(f"{reverse('marketing:landing')}#contacto")
