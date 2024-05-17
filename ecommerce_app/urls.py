from django.urls import path
from .views import index, create_product, list_products, view_cart_products, add_products_to_cart, \
    remove_products_from_cart

app_name = 'ecommerce_app'

urlpatterns = [
    path('', index, name='index'),
    path('product/', list_products, name='product_list'),
    path('product/create/', create_product, name='product_create'),

    path('view_cart_products/', view_cart_products, name='view_cart_products'),
    path('add_products_to_cart/', add_products_to_cart, name='add_products_to_cart'),
    path('remove_products_from_cart/', remove_products_from_cart, name='remove_products_from_cart'),
]
