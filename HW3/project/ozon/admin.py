from django.contrib import admin

# Register your models here.
from .models import Profile, Product, Order

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Order)
