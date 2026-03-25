from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    messages.error(request, "Logged out successfully")
    return redirect('users:login')

def user_profile(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to view this page")
        return redirect('users:login')
    Data_list = {
        'username': request.user.username,
        'email': request.user.email,
        'password': request.user.password,
    }
    return render(request, 'users/profile.html' , Data_list)

def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            messages.error(request, "Username already exists")
            return redirect('users:signup')
        except:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "User created successfully")
            return redirect('users:login')
    return render(request, 'users/register.html')

def delete_account(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to view this page")
        return redirect('users:login')
    user = request.user
    user.delete()
    messages.success(request, "Account deleted successfully")
    return redirect('users:login')