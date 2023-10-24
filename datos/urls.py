from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='profile'),
    path('register/', views.register, name='register'),
]