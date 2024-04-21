# clothes/models.py

from django.db import models

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10)
    
    def __str__(self) :
        return self.name

