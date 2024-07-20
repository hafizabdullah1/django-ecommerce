from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('auth/', include('auth_app.urls')),
    path('cart/', include('cart.urls')),
]
