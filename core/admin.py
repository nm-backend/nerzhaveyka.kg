from django.contrib import admin

from .models import ContactSubmission, GalleryImage, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "in_stock", "is_sale", "is_new", "is_hit", "sort_order", "updated_at")
    list_filter = ("category", "in_stock", "is_sale", "is_new", "is_hit")
    search_fields = ("name", "category", "description")
    list_editable = ("price", "in_stock", "is_sale", "is_new", "is_hit", "sort_order")
    ordering = ("sort_order", "name")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "sort_order", "created_at")
    search_fields = ("title", "description")
    list_editable = ("sort_order",)
    ordering = ("sort_order", "-created_at")


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "source", "is_processed", "created_at")
    list_filter = ("is_processed", "source", "created_at")
    search_fields = ("name", "phone", "message")
    readonly_fields = ("name", "phone", "message", "source", "created_at")
    list_editable = ("is_processed",)
    ordering = ("-created_at",)
