# Generated by Django 4.2.1 on 2023-06-05 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0011_rename_offer_id_skills_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='offer',
            new_name='offer_id',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='skill',
        ),
        migrations.AddField(
            model_name='skills',
            name='id',
            field=models.BigAutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
