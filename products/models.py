from django.db import models
from datetime import datetime

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(**NULLABLE, verbose_name='description')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, **NULLABLE, verbose_name='category')
    price = models.IntegerField(verbose_name='price')
    date_create = datetime.today().strftime('%d-%m-%Y')
    change_data = models.CharField(**NULLABLE, verbose_name='change_data')

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    number_version = models.CharField(max_length=10, verbose_name='number_version')
    name_version = models.CharField(max_length=30, verbose_name='name_version')
    active_version = models.BooleanField(verbose_name='actual_version', default=True)

    def __str__(self):
        return f"{self.product} - {self.name_version} - {self.active_version}"

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'
