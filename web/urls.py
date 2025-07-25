from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("works/", views.works, name="works"),
    path("work-single/<str:id>", views.workSingle, name="work-single"),
    path("services/", views.services, name="services"),
    path("service-single/<str:id>", views.serviceSingle, name="service-single"),
]