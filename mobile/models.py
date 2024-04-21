# book/models.py

from django.db import models

class Mobile(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    des = models.CharField(max_length =150)
    def __str__(self) :
        return self.id
