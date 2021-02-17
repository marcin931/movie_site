from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import movieSerializer
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class movieViewSet ( viewsets.ModelViewSet ):
    queryset = movie.objects.all()
    serializer_class = movieSerializer
    permission_classes = [IsAuthenticated]


def home_view(request):
    products = movie.objects.all()
    context = {'products': products}
    return render(request, 'strona/home.html', context)


def danyFilm(request, id):
    danyFilm_user =movie.objects.get(pk = id)
    return HttpResponse(request, danyFilm_user)


def cart(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items': items}
    return render(request, 'strona/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'strona/checkout.html', context)