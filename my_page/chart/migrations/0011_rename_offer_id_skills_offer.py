# Generated by Django 4.2.1 on 2023-06-04 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0010_rename_brand_id_brands_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='offer_id',
            new_name='offer',
        ),
    ]
