from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Agence (models.Model):

    nom =  models.CharField(max_length=30)
    responsable = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)
    ville = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Client (models.Model):
    
    company_name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    turnover = models.CharField(max_length=30)
    taille = models.IntegerField(default=0)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name

class Contact(models.Model):
    
    email=models.EmailField()
    subject= models.CharField(max_length=20)
    message= models.TextField(max_length=150)

    def __str__(self):
        return self.email
    
