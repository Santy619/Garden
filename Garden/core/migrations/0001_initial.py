# Generated by Django 4.0.1 on 2023-01-18 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('idPlanta', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de planta')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre de planta')),
                ('precio', models.IntegerField(blank=True, max_length=20, null=True, verbose_name='precio')),
                ('stock', models.IntegerField(blank=True, null=True, verbose_name='Modelo')),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]