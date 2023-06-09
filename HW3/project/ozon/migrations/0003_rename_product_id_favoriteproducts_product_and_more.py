# Generated by Django 4.2 on 2023-05-04 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ozon', '0002_favoriteproducts_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoriteproducts',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='favoriteproducts',
            old_name='profile_id',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='profile_id',
            new_name='profile',
        ),
        migrations.AlterField(
            model_name='favoriteproducts',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 22, 17, 56, 806856)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 22, 17, 56, 805856)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 22, 17, 56, 804856)),
        ),
    ]
