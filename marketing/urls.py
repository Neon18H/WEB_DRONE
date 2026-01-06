from django.urls import path

from marketing import views

app_name = "marketing"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("landing/", views.landing, name="landing_alt"),
    path("contact/", views.contact_submit, name="contact_submit"),
    path("thank-you/", views.thank_you, name="thank_you"),
]
