from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import movieSerializer
from rest_framework.permissions import IsAuthenticated
import json


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
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items': items, 'order': order}
    return render(request, 'strona/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'strona/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user
    product = movie.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete= False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('item was added', safe = False)

