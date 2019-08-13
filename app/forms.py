from django import forms
from .models import Hood,Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        exclude = ['admin']
