# Generated by Django 2.0 on 2024-12-12 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animaldetectapp', '0003_animals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animals',
            old_name='conservation_status',
            new_name='endangered_status',
        ),
    ]
