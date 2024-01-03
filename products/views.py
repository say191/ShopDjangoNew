# from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView, DetailView


# def catalog(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Store - Our products'
#     }
#     return render(request, 'products/product_list.html', context)

class ProductListView(ListView):
    model = Product


# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#     }
#     return render(request, 'products/product_detail.html', context)

class ProductDetailView(DetailView):
    model = Product
