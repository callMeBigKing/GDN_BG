from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    payment = models.CharField(max_length=50)