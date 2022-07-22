from django.db import models

# Create your models here.
class member(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20,)
    email = models.CharField(max_length=255, unique=True)

    
class members(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20,)
    email = models.CharField(max_length=255, unique=True)
    Name = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)