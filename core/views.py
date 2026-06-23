from django.shortcuts import render

from .models import GalleryImage, Product


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def products(request):
    queryset = Product.objects.filter(in_stock=True)

    category = request.GET.get("category")
    if category:
        queryset = queryset.filter(category__iexact=category)

    price_from = request.GET.get("price_from")
    price_to = request.GET.get("price_to")
    if price_from:
        queryset = queryset.filter(price__gte=price_from)
    if price_to:
        queryset = queryset.filter(price__lte=price_to)

    products_list = queryset.order_by("sort_order", "name")
    categories = (
        Product.objects.filter(in_stock=True)
        .exclude(category="")
        .values_list("category", flat=True)
        .distinct()
        .order_by("category")
    )

    return render(
        request,
        "products.html",
        {
            "products": products_list,
            "categories": categories,
            "active_category": category or "",
        },
    )


def gallery(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, "gallery.html", {"gallery_images": gallery_images})


def contacts(request):
    return render(request, "contacts.html")
