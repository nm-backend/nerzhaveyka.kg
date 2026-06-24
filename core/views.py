from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import GalleryImage, Product


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def products(request):
    queryset = Product.objects.filter(in_stock=True)

    category = request.GET.get("category", "").strip()
    if category:
        queryset = queryset.filter(category__iexact=category)

    search = request.GET.get("q", "").strip()
    if search:
        queryset = queryset.filter(
            Q(name__icontains=search)
            | Q(description__icontains=search)
            | Q(category__icontains=search)
        )

    price_min = request.GET.get("price_min", "").strip()
    price_max = request.GET.get("price_max", "").strip()
    if price_min:
        queryset = queryset.filter(price__gte=price_min)
    if price_max:
        queryset = queryset.filter(price__lte=price_max)

    if request.GET.get("is_sale") == "1":
        queryset = queryset.filter(is_sale=True)
    if request.GET.get("is_new") == "1":
        queryset = queryset.filter(is_new=True)
    if request.GET.get("is_hit") == "1":
        queryset = queryset.filter(is_hit=True)

    queryset = queryset.order_by("sort_order", "name")
    categories = (
        Product.objects.filter(in_stock=True)
        .exclude(category="")
        .values_list("category", flat=True)
        .distinct()
        .order_by("category")
    )

    paginator = Paginator(queryset, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    params = request.GET.copy()
    params.pop("page", None)
    querystring = params.urlencode()

    return render(
        request,
        "products.html",
        {
            "page_obj": page_obj,
            "products": page_obj.object_list,
            "categories": categories,
            "active_category": category,
            "filters": request.GET,
            "querystring": querystring,
        },
    )


def gallery(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, "gallery.html", {"gallery_images": gallery_images})


def contacts(request):
    return render(request, "contacts.html")
