# Generated by Django 4.2.1 on 2023-06-04 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0008_rename_offer_id_employmenttypes_offer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='offer',
            new_name='offer_id',
        ),
    ]
