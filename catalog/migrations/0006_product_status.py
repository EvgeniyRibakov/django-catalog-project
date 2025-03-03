# Generated by Django 5.1.4 on 2025-02-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовано')], default='draft', help_text='Укажите статус публикации продукта', max_length=10, verbose_name='Статус публикации'),
        ),
    ]
