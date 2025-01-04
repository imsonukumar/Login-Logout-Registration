from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        my_user = User.objects.create_user(username, email, pass1)
        my_user.save()
        return redirect('login')
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user is None:
            messages.error(request, 'User not found')
            return redirect('login')
        
        user = authenticate(request,username=username, password=password)
        if user is None:
            messages.error(request, 'Wrong password')
            return redirect('login')
        login(request, user)
        return redirect('home')
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')