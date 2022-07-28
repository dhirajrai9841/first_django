from unittest.util import _MAX_LENGTH 
from django.db import models
from sqlalchemy import true

class registeredUsers(models.Model):
    username=models.CharField(max_length=225)
    firstname=models.TextField(null=true)
    lastname=models.TextField(null=true)
    Dateofbirth=models.IntegerField(max_length=10,null=true)
    email=models.CharField(max_length=225,null=true)
    password=models.CharField(max_length=225,null=true)
    Reenterpassword=models.CharField(max_length=225,null=true)
    post=models.TextField(null=true)


 
 
 
 
 

 




# Create your models here.
