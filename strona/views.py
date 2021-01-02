from django.shortcuts import render, redirect
from .models import movie
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework import generics
from .serializers import movieSerializer

# Create your views here.

class movieList(generics.ListCreateAPIView):
    queryset = movie.objects.all()
    serializer_class = movieSerializer

class movieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = movie.objects.all()
    serializer_class = movieSerializer



def home_view(request):
    zapytanie = movie.objects.all()
    dane = {'zapytanie': zapytanie}
    return render(request, 'strona/home.html', dane)

def danyFilm(request, id):
    danyFilm_user = movie.objects.get(pk = id)
    return HttpResponse(danyFilm_user.description)

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