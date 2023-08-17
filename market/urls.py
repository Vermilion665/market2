"""
URL configuration for market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import urls as products_urls
from users import urls as users_urls
from cart import urls as cart_urls
from orders import urls as orders_urls
from products.views import root_index

urlpatterns = [
    path('', root_index, name='root_index'),
    path('admin/', admin.site.urls),
    path('shop/', include(products_urls)),
    path('users/', include(users_urls)),
    path('orders/', include(orders_urls)),
    path('cart/', include(cart_urls)),
]
