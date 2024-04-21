from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return '%s %s %s %s' % (self.fname,self.lname,self.email,self.password)