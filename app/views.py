from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

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
@login_required(login_url='/accounts/login/')
def edit_profile(request):
    """
    View function to handle profile edit requests
    """
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = current_user
            prof.save()
            return redirect('prof')
    else:
        form = ProfileForm()
    return render(request, 'all-templates/edit.html', {'form': form, 'profile':profile})

