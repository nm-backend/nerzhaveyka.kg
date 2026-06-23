from rest_framework import generics, status
from rest_framework.response import Response

from core.models import ContactSubmission, Product

from .serializers import ContactSubmissionSerializer, ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(in_stock=True).order_by("sort_order", "name")
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category__iexact=category)
        return queryset


class ContactSubmissionCreateAPIView(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                "status": "success",
                "message": "Спасибо! Ваша заявка принята. Мы скоро свяжемся с вами.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
