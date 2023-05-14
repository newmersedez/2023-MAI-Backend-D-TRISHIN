import datetime

from django.db import models

class Profile(models.Model):
    email = models.TextField(blank=False, default='')
    password = models.TextField(blank=False, default='')
    registration_date = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.TextField(blank=False, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    created_date = models.DateTimeField(blank=False, default=datetime.datetime.utcnow, verbose_name='Дата создания')

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False, verbose_name='Связанный продукт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, verbose_name='Связанный пользователь')
    shipping_address = models.TextField(blank=False, verbose_name='Адрес доставки')
    created_date = models.DateTimeField(default=datetime.datetime.utcnow, blank=False, verbose_name='Дата создания')

    class Meta:
        db_table = 'orders'
