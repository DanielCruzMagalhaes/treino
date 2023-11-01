from django.db import models

# Create your models here.
from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    publicação = models.DateField()
    paginas = models.IntegerField()