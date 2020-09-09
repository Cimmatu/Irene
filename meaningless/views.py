from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def home_view(request):
    context = {}
    return render(request, 'meaningless/index.html', context)


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    
    return render(request, 'meaningless/login.html', context)


def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'meaningless/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
