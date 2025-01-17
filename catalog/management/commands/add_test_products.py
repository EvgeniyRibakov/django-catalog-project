from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных после очистки'

    def handle(self, *args, **kwargs):
        # Удаляем все продукты и категории
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем тестовые категории
        categories = [
            Category(name='Электроника', description='Описание электроники'),
            Category(name='Одежда', description='Описание одежды'),
            Category(name='Продукты', description='Описание продуктов'),
        ]
        Category.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS(f'Создано {len(categories)} категорий.'))

        # Создаем тестовые продукты
        products = [
            Product(
                name='Смартфон',
                description='Современный смартфон с отличной камерой',
                image=None,
                category=categories[0],
                price=15000,
            ),
            Product(
                name='Футболка',
                description='Хлопковая футболка',
                image=None,
                category=categories[1],
                price=500,
            ),
            Product(
                name='Яблоки',
                description='Свежие яблоки',
                image=None,
                category=categories[2],
                price=200,
            ),
        ]
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'Создано {len(products)} продуктов.'))

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены!'))
