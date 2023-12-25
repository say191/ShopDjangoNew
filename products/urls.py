from django.urls import path
from products.views import index, product


urlpatterns = [
    path('', index),
    path('<int:pk>/product/', product, name='product'),
]