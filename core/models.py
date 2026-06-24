from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=200)
    category = models.CharField("Категория", max_length=120, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="products/", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, blank=True, null=True)
    in_stock = models.BooleanField("В наличии", default=True)
    is_sale = models.BooleanField("Товар по акции", default=False)
    is_new = models.BooleanField("Новинка", default=False)
    is_hit = models.BooleanField("Хит", default=False)
    sort_order = models.PositiveIntegerField("Порядок", default=0)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField("Название", max_length=200)
    image = models.ImageField("Изображение", upload_to="gallery/")
    description = models.TextField("Описание", blank=True)
    sort_order = models.PositiveIntegerField("Порядок", default=0)
    created_at = models.DateTimeField("Добавлено", auto_now_add=True)

    class Meta:
        verbose_name = "Фото галереи"
        verbose_name_plural = "Галерея"
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    name = models.CharField("Имя", max_length=120)
    phone = models.CharField("Телефон", max_length=40)
    message = models.TextField("Комментарий", blank=True)
    source = models.CharField("Источник", max_length=80, default="site_form")
    is_processed = models.BooleanField("Обработано", default=False)
    created_at = models.DateTimeField("Дата заявки", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.phone}"
