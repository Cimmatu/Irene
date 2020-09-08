from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def home_view(request):
    context = {}
    return render(request, 'meaningless/index.html', context)


def login_view(request):
    context = {}
    return render(request, 'meaningless/login.html', context)


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'meaningless/register.html', context)

