# Generated by Django 4.1.2 on 2023-07-07 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0010_alter_pelicula_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(null=True, upload_to='static'),
        ),
    ]
