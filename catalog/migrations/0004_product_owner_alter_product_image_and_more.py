# Generated by Django 5.1.4 on 2025-02-12 14:09

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_views_counter'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='Укажите создателя', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите фото продукта', null=True, upload_to='catalog/image/', verbose_name='Фото продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000)], verbose_name='Цена за продукт'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(blank=True, help_text='Введите дату последнего изменения', null=True, verbose_name='Дата последнего изменения'),
        ),
    ]
