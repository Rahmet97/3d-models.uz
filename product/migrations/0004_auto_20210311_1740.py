# Generated by Django 3.1.1 on 2021-03-11 12:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_cart_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000)], verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000)], verbose_name='Price'),
        ),
    ]