from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

def get_absolute_url(self):
    """
     Devuelve la url para acceder a una instancia particular del modelo.
    """
    return reverse('model-detail-view', args=[str(self.id)])


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text='Introduce Nombre del Director')

    def __str__(self):
        return self.name

class Peliculas(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('Directores', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Pon aqui resumen de la pelicula')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])


class Directores(models.Model):
    """
    Modelo que representa un autor
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)
