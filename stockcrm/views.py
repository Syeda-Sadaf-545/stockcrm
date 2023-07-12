from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# here we do coding for login & authentication


def home(request):
    # Check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In ')
            # after login we want user to re-direct so;
            return redirect('home')
        else:
            messages.success(request, "There was an error! Please Try Again")
            return redirect('home')
    return render(request, 'home.html', {})

# bana skty he login ka separate function bhi but wo hamny home par hi likhdia he
# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out!")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})
