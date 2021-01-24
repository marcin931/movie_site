from . import views
from django.urls import path

app_name = 'account'
urlpatterns = [

    path('signup/', views.SignupView.as_view(), name = 'signup'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
]
