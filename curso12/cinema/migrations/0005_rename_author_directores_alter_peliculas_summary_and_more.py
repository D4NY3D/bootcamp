# Generated by Django 4.0.5 on 2022-07-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_rename_pelis_peliculas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Directores',
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='summary',
            field=models.TextField(help_text='Pon aqui resumen de la pelicula', max_length=1000),
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
    ]
