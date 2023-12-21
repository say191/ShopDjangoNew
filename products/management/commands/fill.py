from django.core.management import BaseCommand
from products.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        phones = Category(name='Phones').save()
        laptops = Category(name='Laptops').save()
        tv = Category(name='TV').save()

        product_list = [
            {'name': 'q1', 'price': 100000, 'category': phones},
            {'name': 'w2', 'price': 80000, 'category': phones},
            {'name': 'e3', 'price': 200000, 'category': laptops},
            {'name': 'r4', 'price': 50000, 'category': laptops},
            {'name': 't5', 'price': 120000, 'category': tv},
            {'name': 'y6', 'price': 150000, 'category': tv}
        ]

        products_for_create = []
        for product_item in product_list:
            products_for_create.append(Product(**product_item))
        Product.objects.bulk_create(products_for_create)
