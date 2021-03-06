# Generated by Django 3.1.1 on 2021-04-17 21:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210418_0007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Model rasmi'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'published_at', 'updated_at'], 'verbose_name': '3D Model', 'verbose_name_plural': '3D Modellar'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='category/%Y/%m/%d/', verbose_name='Kategoriya rasmi'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Kategoriya'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Kategoriya'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Kategoriya'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_uz',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Kategoriya'),
        ),
        migrations.AlterField(
            model_name='images',
            name='caption',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Titr:'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='product-images/%Y/%m/%d/', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='caption',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Titr'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.category', verbose_name='Kategoriya'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Tavsif'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000)], verbose_name='Chegirma'),
        ),
        migrations.AlterField(
            model_name='product',
            name='downloaded',
            field=models.IntegerField(default=0, verbose_name='Yuklab olindi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='free',
            field=models.BooleanField(default=False, verbose_name='Bepul'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='product/%Y/%m/%d/', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model_file',
            field=models.FileField(null=True, upload_to='3D_File/%Y/%m/%d/', verbose_name='Model Fayl'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=300, null=True, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_uz',
            field=models.CharField(max_length=300, null=True, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='paid',
            field=models.BooleanField(default=True, verbose_name='Pullik'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000)], verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_info',
            field=models.CharField(default='3D model', max_length=500, verbose_name="Qisqa ma'lumot"),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_info_en',
            field=models.CharField(default='3D model', max_length=500, null=True, verbose_name="Qisqa ma'lumot"),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_info_ru',
            field=models.CharField(default='3D model', max_length=500, null=True, verbose_name="Qisqa ma'lumot"),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_info_uz',
            field=models.CharField(default='3D model', max_length=500, null=True, verbose_name="Qisqa ma'lumot"),
        ),
    ]
