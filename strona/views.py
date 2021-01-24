from django.shortcuts import render, redirect
from .models import movie
from django.http import HttpResponse
from django.contrib.auth import login, logout
from rest_framework import viewsets
from .serializers import movieSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class movieViewSet ( viewsets.ModelViewSet ):
    queryset = movie.objects.all()
    serializer_class = movieSerializer
    permission_classes = [IsAuthenticated]


def home_view(request):
    zapytanie = movie.objects.all ()
    dane = {'zapytanie': zapytanie}
    return render(request, 'strona/home.html', dane)


def danyFilm(request, id):
    danyFilm_user =movie.objects.get(pk = id )
    return HttpResponse(request, danyFilm_user)