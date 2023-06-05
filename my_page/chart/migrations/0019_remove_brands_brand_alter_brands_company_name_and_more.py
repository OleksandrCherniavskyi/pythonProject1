# Generated by Django 4.2.1 on 2023-06-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0018_rename_offer_id_offers_id_rename_skill_id_skills_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brands',
            name='brand',
        ),
        migrations.AlterField(
            model_name='brands',
            name='company_name',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='offers',
            name='company_name',
            field=models.CharField(max_length=250),
        ),
    ]
