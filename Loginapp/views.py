
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Login Success")
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', context={'message': True})
    else:
        if not request.user.is_authenticated:
            return render(request, 'login.html', context={'message': False})
        else:
            return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/login/')
