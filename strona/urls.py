from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name = 'strona-home'),
    path('danyFilm/<id>', views.danyFilm, name = 'danyFilm')
]
