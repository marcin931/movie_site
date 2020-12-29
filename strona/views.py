from django.shortcuts import render, redirect
from .models import Filmy
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def home_view(request):
    zapytanie = Filmy.objects.all()
    dane = {'zapytanie': zapytanie}
    return render(request, 'strona/home.html', dane)

def danyFilm(request, id):
    danyFilm_user = Filmy.objects.get(pk = id)
    return HttpResponse(danyFilm_user.title)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'strona/home.html')
    else:
            form = SignUpForm()
    return render(request, 'strona/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'strona/home.html')
    else:
        form = LoginForm()
    return render(request,'strona/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'strona/home.html')