# Generated by Django 4.0.1 on 2023-01-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_planta_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='imagen',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Imagen'),
        ),
    ]
