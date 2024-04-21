# book/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    des = models.CharField(max_length =150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self) :
        return self.title
