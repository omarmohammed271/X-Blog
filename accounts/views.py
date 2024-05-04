from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .models import Profile
# Create your views here.

def login_view(request):

    return render(request,'accounts/login.html')

def login_view(request):
    logout(request)
    return redirect('home')


