from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    type=models.CharField(max_length=10,blank=True,null=True)
    phone=models.CharField(max_length=12,blank=True,null=True)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]


class TpoProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    min_ctc=models.CharField(max_length=10)
    desc=models.CharField(max_length=100)
    status=models.CharField(max_length=10,default="HIRING")
    image=models.ImageField(default='default1.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.name}'

    
    

class CompanyProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    location=models.CharField(max_length=25)
    desc=models.CharField(max_length=100)
    sector=models.CharField(max_length=20)
    image=models.ImageField(default='default2.jpg',upload_to='profile_pics')

    def __str__(self):
     return f'{self.user.name}'


