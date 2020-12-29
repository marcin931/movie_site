from django.urls import path
from . import views

app_name = 'strona'
urlpatterns = [
    path('', views.home_view, name = 'strona-home'),
    path('danyFilm/<id>', views.danyFilm, name = 'danyFilm'),
    path('signup/', views.signup_view, name = 'signup'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
]
