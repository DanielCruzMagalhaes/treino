from django.shortcuts import render
from .models import Livro



def lista_livros(request):
    livros = Livro.object.all()
    return render(request, 'lista_livros.html',{'livros': livros})

# Create your views here.
