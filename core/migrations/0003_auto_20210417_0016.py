# Generated by Django 3.1.1 on 2021-04-16 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210409_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='description_en_us',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='title_en_us',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='description_en_us',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='name_en_us',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='videomodel',
            old_name='description_en_us',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='videomodel',
            old_name='title_en_us',
            new_name='title_en',
        ),
    ]
