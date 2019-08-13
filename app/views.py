from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *

# Create your views here.
def index(request):
    """
    View function to render the homepage
    """
    neighbourhoods = Hood.objects.all()
    try:
        current_user=request.user
        # profile =Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('edit')
    return render(request,"all-templates/index.html",{"neighbourhood":neighbourhoods})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    # profile = User.objects.get(username=username)
    # print(profile.id)
    try:
        profiles = Profile.get_by_id(profile.id)
    except:
        profiles = Profile.filter_by_id(profile.id)

    return render(request, 'all-templates/profile.html', {'profiles':profiles})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('prof',username=request.user)
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form})

@login_required(login_url='/accounts/login/')
def addneighbourhood(request):
    neighbourform = NeighbourhoodForm()
    if request.method == "POST":
        neighbourform = NeighbourhoodForm(request.POST, request.FILES)
        if neighbourform.is_valid():
            upload = neighbourform.save(commit=False)
            upload.save()
            return redirect('index')
        else:
            neighbourform = NeighbourhoodForm(request.POST, request.FILES)
    return render(request, 'all-templates/hood.html', {"neighbourform": neighbourform})