from django.urls import path
from .views import *

urlpatterns = [
    path('', products_page, name='dashboard_products'),
    path('categories/', categories_page, name='dashboard_categories'),
    # Product related urls
    path('create_product/', create_product, name='create_product'),
    path('update_product/<int:id>/', update_product, name='update_product'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    # Product related urls
    path('create_category/', create_category, name='create_category'),
    path('update_category/<int:id>/', update_category, name='update_category'),
    path('delete_category/<int:id>/', delete_category, name='delete_category'),
]
