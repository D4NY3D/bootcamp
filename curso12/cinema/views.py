from django.shortcuts import render

# Create your views here.

from .models import Peliculas, Directores, Genre

def index(request):
    num_books = Peliculas.objects.all().count()
    num_author = Directores.objects.all().count()


    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_authors': num_author
        }
    )