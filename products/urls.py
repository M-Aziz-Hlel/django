from django.urls import path
from .views import my_products,add_category,add_product,edit_product,delete_product

urlpatterns = [
    path("", my_products, name="home"),
    path("add/", add_product, name="add-product"),
    path("category/add/", add_category, name="add-category"),

    path("<int:pk>/edit/", edit_product, name="edit-product"),
    path("<int:pk>/delete/", delete_product, name="delete-product"),


]