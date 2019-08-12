from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to = 'media/')
    bio = models.TextField(default="Hey there!I\'m using Instagram")
    location = models.CharField(max_length = 60,default='Somewhere')
    neighbourhood_name = models.CharField(max_length=20,default='Nameless')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
