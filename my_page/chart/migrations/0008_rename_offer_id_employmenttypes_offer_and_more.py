# Generated by Django 4.2.1 on 2023-06-04 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0007_remove_employmenttypes_employment_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employmenttypes',
            old_name='offer_id',
            new_name='offer',
        ),
        migrations.RenameField(
            model_name='skills',
            old_name='offer_id',
            new_name='offer',
        ),
    ]