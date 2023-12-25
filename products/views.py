from django.shortcuts import render
from products.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Store - Our products'
    }
    return render(request, 'products/index.html', context)


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
    }
    return render(request, 'products/product.html', context)