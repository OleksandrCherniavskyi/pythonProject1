# Generated by Django 4.2.1 on 2023-06-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0015_rename_skill_id_skills_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='id',
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]
