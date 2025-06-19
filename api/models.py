from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100) 
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=15, decimal_places=2)      

    def __str__(self):
        return self.title
    