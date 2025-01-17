from django.db import models
from django.core.validators import MaxValueValidator


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="catalog/image/",  # Папка для хранения изображений
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Загрузите фото продукта",
    )
    category = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите категорию",
    )
    price = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10000)],
        verbose_name="Цена за продукт",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


# Model representing a Category entity
class Category(models.Model):
    """Represents a category with name and optional description."""

    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",  # Display name for admin panel
        help_text="Введите название категории",  # Tooltip/help text in admin panel
    )
    description = models.TextField(
        blank=True,  # Field is optional
        null=True,  # Allows storing null values
        verbose_name="Описание категории",  # Display name for admin panel
        help_text="Введите описание категории",  # Tooltip/help text in admin panel
    )

    # Meta information for the Category model
    class Meta:
        verbose_name = "Категория"  # Singular name for admin panel
        verbose_name_plural = "Категории"  # Plural name for admin panel

    # String representation of the Category object
    def __str__(self):
        return self.name