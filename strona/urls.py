from django.urls import path, include
from . import views

from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'movie', views.movieViewSet)

app_name = 'strona'
urlpatterns = [

    path('', views.home_view, name = 'strona-home'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('danyFilm/<id>', views.danyFilm, name = 'danyFilm'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),


]

