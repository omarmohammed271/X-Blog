from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Profile
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user:
            login(request,user)
            return redirect('blog:blog')
        else:
            return render(request,'accounts/login.html',{'error':'Invalid email or password'})
            
    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def register(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username=email,email=email,password=password1)
            return redirect('blog:blog')
        else:
            return render(request,'accounts/register.html',{'error':'Invalid password and confirm password'})


    return render(request,'accounts/register.html')



