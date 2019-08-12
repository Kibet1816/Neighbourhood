from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    Model class for a single user
    """
    photo = models.ImageField(upload_to = 'media/')
    bio = models.TextField(default="Hey there!I\'m using Instagram")
    location = models.CharField(max_length = 60,default='Somewhere')
    neighbourhood_name = models.CharField(max_length=20,default='Nameless')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile
    
class Neighbourhood(models.Model):
    """
    Model class for a single neighbourhood
    """
    name = models.CharField(max_length = 60)
    location = models.CharField(max_length =60)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default=1)