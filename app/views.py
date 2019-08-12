from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    """
    View function to render the homepage
    """
    try:
        current_user=request.user
        profile =Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('edit')
    return render(request,"all-templates/index.html")

@login_required(login_url='/accounts/login/')
def profile(request):
    """
    View function to render the homepage
    """
    return render(request,"all-templates/profile.html")

