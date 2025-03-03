from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_name):
    """Возвращает список продуктов в указанной категории."""
    cache_key = f"products_category_{category_name}"
    products = cache.get(cache_key)
    if not products:
        products = Product.objects.filter(category=category_name)
        cache.set(cache_key, products, timeout=60 * 15)  # Кэш на 15 минут
    return products
