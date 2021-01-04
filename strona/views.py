from django.shortcuts import render, redirect
from .models import movie
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout
from rest_framework import viewsets
from .serializers import movieSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class movieViewSet ( viewsets.ModelViewSet ):
    queryset = movie.objects.all ()
    serializer_class = movieSerializer
    permission_classes = [IsAuthenticated]


def home_view ( request ):
    zapytanie = movie.objects.all ()
    dane = {'zapytanie': zapytanie}
    return render ( request, 'strona/home.html', dane )


def danyFilm(request, id):
    danyFilm_user =movie.objects.get(pk = id )
    return HttpResponse(request, danyFilm_user)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('strona:strona-home')
    else:
        form = SignUpForm()
    return render(request, 'strona/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('strona:strona-home')
    else:
         form = LoginForm()
    return render(request, 'strona/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('strona:strona-home')
