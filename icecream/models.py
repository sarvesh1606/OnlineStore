from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Contact(models.Model):
    
    name=models.CharField(max_length=122 , default='' ) 
    email=models.CharField(max_length=122 , default='' )
    phone=models.CharField(max_length=122 , default='')
    order=models.CharField(max_length=122 , default='')
    time=models.CharField(max_length=122 , default='' )
    ice=models.CharField(max_length=122 , default='')
    instruct=models.CharField(max_length=122 , default='')
    date=models.DateField() 

    def __str__(self):
        return self.name

class Signup(models.Model):
    
    user= models.OneToOneField(User ,null=True,  on_delete=models.CASCADE )
    username=models.CharField(max_length=122)
    fname=models.CharField(max_length=122 )

    def __str__(self):
        return self.fname
    