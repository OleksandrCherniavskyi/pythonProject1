# Generated by Django 4.2.1 on 2023-06-03 12:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0006_rename_offer_skills_offer_id_remove_brands_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employmenttypes',
            name='employment_id',
        ),
        migrations.AddField(
            model_name='employmenttypes',
            name='offer_id',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='chart.offers'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employmenttypes',
            name='employment_type_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='offers',
            name='offer_id',
            field=models.CharField(default=datetime.datetime.now, max_length=300, primary_key=True, serialize=False),
        ),
    ]
