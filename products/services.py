from django.core.cache import cache
from django.conf import settings
from products.models import Category


def get_cache_categories():
    if settings.CACHES_ENABLED:
        category_list = cache.get('category_list')
        if category_list is None:
            category_list = Category.objects.all()
            cache.set('category_list', category_list)
    else:
        category_list = Category.objects.all()
        return category_list
