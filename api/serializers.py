from rest_framework import serializers

from core.models import ContactSubmission, Product


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "description",
            "image_url",
            "price",
            "in_stock",
        )

    def get_image_url(self, product):
        request = self.context.get("request")
        if not product.image:
            return ""
        if request:
            return request.build_absolute_uri(product.image.url)
        return product.image.url


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ("id", "name", "phone", "message", "created_at")
        read_only_fields = ("id", "created_at")

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Введите имя.")
        return value

    def validate_phone(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Введите номер телефона.")
        return value
