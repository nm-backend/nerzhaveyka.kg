from django.urls import path

from .views import ContactSubmissionCreateAPIView, ProductListAPIView

app_name = "api"

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="product-list"),
    path("contacts/submit/", ContactSubmissionCreateAPIView.as_view(), name="contact-submit"),
]
