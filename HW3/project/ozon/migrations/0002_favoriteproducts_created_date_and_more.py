# Generated by Django 4.2 on 2023-05-04 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ozon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteproducts',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 22, 17, 15, 712584)),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 22, 17, 15, 711588)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 22, 17, 15, 709584)),
        ),
    ]
