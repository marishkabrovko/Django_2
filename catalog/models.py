from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория", help_text="Введите категорию товара")
    description = models.TextField(verbose_name="Описание категории", help_text="Введите описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Товар", help_text="Введите название товара")
    description = models.TextField(verbose_name="Описание товара", help_text="Введите описание товара")
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение товара",
        help_text="Загрузите изображение товара",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию",
        related_name="products",
        null=True,
        blank=True,
    )
    price = models.FloatField(verbose_name="Цена товара", help_text="Введите цену товара")
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
        