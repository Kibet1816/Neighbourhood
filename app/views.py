from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """
    View function to render the homepage
    """
    return render(request,"all-templates/index.html")

@login_required(login_url='/accounts/login/')
def profile(request):
    """
    View function to render the homepage
    """
    return render(request,"all-templates/profile.html")