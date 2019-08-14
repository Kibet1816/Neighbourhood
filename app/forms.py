from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['admin']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['name','hood','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
