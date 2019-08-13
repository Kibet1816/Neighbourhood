from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    Model class for a single user
    """
    photo = models.ImageField(upload_to='media/')
    bio = models.TextField(default="Hey there!I\'m using Instagram")
    location = models.CharField(max_length=60, default='Somewhere')
    neighbourhood_name = models.CharField(max_length=20, default='Nameless')
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile


class Neighbourhood(models.Model):
    """
    Model class for a single neighbourhood
    """
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Hood(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    population = models.IntegerField()
    admin = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    landing_page = models.ImageField(upload_to='photos', null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @classmethod
    def search_hood(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood
