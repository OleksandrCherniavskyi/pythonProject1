# Generated by Django 4.2.1 on 2023-06-04 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0009_rename_offer_skills_offer_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brands',
            old_name='brand_id',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='brandsoffice',
            old_name='office_id',
            new_name='brand_office',
        ),
        migrations.RenameField(
            model_name='employmenttypes',
            old_name='employment_type_id',
            new_name='employment_type',
        ),
        migrations.RenameField(
            model_name='offers',
            old_name='offer_id',
            new_name='offer',
        ),
        migrations.RenameField(
            model_name='skills',
            old_name='skill_id',
            new_name='skill',
        ),
    ]
