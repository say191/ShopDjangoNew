from django.urls import path
from products.views import catalog, product
from products.apps import ProductsConfig

app_name = ProductsConfig.name
urlpatterns = [
    path('', catalog),
    path('<int:pk>/product/', product, name='product'),
]