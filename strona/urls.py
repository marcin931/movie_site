from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'strona'
urlpatterns = [
    path('', views.home_view, name = 'strona-home'),
    path('danyFilm/<id>', views.danyFilm, name = 'danyFilm'),
    path('signup/', views.signup_view, name = 'signup'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('strona/', views.movieList.as_view()),
    path('strona/<int:pk>/', views.movieDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
