from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    color = models.CharField(max_length=50, default='white')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    brand = models.CharField(max_length=20)
    colors = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    countInStock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title