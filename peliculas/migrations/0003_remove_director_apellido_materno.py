# Generated by Django 4.1.2 on 2023-06-24 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_rename_alumno_pelicula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='apellido_materno',
        ),
    ]
