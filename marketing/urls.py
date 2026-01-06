from django.urls import path

from marketing import views

app_name = "marketing"

urlpatterns = [
    path("", views.landing_view, name="landing"),
    path("contact/", views.contact_submit, name="contact_submit"),
]
