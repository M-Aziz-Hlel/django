from django.urls import path
from .views import my_products

urlpatterns = [
    path("", my_products, name="my-products"),
]