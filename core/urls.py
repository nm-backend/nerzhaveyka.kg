from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("gallery/", views.gallery, name="gallery"),
    path("contacts/", views.contacts, name="contacts"),
]