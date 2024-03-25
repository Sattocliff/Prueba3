# Generated by Django 4.1.2 on 2024-03-24 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0015_alter_pelicula_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='descripcion',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='nombre_pelicula',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]