# Generated by Django 4.1.2 on 2023-06-27 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_remove_director_apellido_materno'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]
