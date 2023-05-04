import datetime

from django.db import models

class Profile(models.Model):
    email = models.TextField()
    password = models.TextField()
    registration_date = models.DateTimeField()

    class Meta:
        db_table = 'profiles'

class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.datetime.utcnow())
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    destination = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.utcnow())

    class Meta:
        db_table = 'orders'


class FavoriteProducts(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.datetime.utcnow())

    class Meta:
        db_table = 'favorite_products'