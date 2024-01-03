from django.urls import path
# from products.views import catalog, product
from products.views import ProductListView, ProductDetailView
from products.apps import ProductsConfig

app_name = ProductsConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
]