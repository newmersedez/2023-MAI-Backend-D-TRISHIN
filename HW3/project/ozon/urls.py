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

from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('profiles/', views.get_profiles, name='all_profiles'),
    path('profile/<int:profile_id>/', views.get_profile, name='specific_profile'),
    path('profiles/', views.create_profile, name='create_profile'),

    path('products/', views.get_products, name='all_products'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:product_id>/', views.get_product, name='specific_product'),

    path('orders/', views.get_orders, name='all_orders'),
    path('orders/create/', views.create_order, name='create_order'),
]
