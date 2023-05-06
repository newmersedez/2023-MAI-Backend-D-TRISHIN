import datetime

from django.db import models

class Profile(models.Model):
    email = models.TextField()
    password = models.TextField()
    registration_date = models.DateTimeField()

    class Meta:
        db_table = 'profiles'

class Product(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    created_date = models.DateTimeField(default=datetime.datetime.utcnow(), verbose_name='Дата создания')
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Создатель')

    class Meta:
        db_table = 'products'

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Связанный продукт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Связанный пользователь')
    destination = models.TextField(verbose_name='Адрес доставки')
    created_date = models.DateTimeField(default=datetime.datetime.utcnow(), verbose_name='Дата создания')

    class Meta:
        db_table = 'orders'


class FavoriteProducts(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Связанный продукт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Связанный пользователь')
    created_date = models.DateTimeField(default=datetime.datetime.utcnow(), verbose_name='Дата создания')

    class Meta:
        db_table = 'favorite_products'
