"""
URL configuration for project project.

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

from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('profile', views.get_current_profile_details),
    path('profile', views.create_profile, name='profile'),

    path('products', views.get_products),
    path('products/', views.create_product, name='products'),
    path('products/<int:product_id>', views.get_product, name='products'),

    path('orders', views.get_orders),
    path('orders', views.create_order, name='orders'),
]