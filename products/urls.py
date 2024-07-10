from django.contrib import admin
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', categories_page, name='categories'),
    path('products/<int:category_id>/', get_products_by_category, name='products'),
    path('product/<int:id>/', get_product_detail, name="product_detail")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)