from django.shortcuts import render
from .models import Filmy
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    zapytanie = Filmy.objects.all()
    dane = {'zapytanie': zapytanie}
    return render(request, 'strona/home.html', dane)

def danyFilm(request, id):
    danyFilm_user = Filmy.objects.get(pk = id)
    return HttpResponse(danyFilm_user.title)