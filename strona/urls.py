from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movie', views.movieViewSet)

app_name = 'strona'
urlpatterns = [
    path('', views.home_view, name = 'strona-home'),
    path('danyFilm/<id>', views.danyFilm, name = 'danyFilm'),
    path('signup/', views.signup_view, name = 'signup'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))

]

