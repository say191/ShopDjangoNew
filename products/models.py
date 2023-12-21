from django.db import models

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
    price = models.FloatField(verbose_name='price')
    date_create = models.DateField(**NULLABLE, verbose_name='date_create')
    change_data = models.DateField(**NULLABLE, verbose_name='change_data')

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
