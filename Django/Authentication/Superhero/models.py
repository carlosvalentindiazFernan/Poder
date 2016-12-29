from django.db import models

# Create your models here.

class hero(models.Model):
    idhero    	=   models.AutoField(primary_key=True)
    name        =   models.CharField(max_length=35)
    age     	=   models.CharField(max_length=10)
    power   	=   models.CharField(max_length=40)
    def __str__(self):
         return self.name
