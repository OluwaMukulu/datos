from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('registerpage/', views.registerpage, name='registerpage'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('listexpenses/', views.listexpenses, name='listexpenses'),
    path('addexpenses/', views.addexpenses, name='addexpenses'),
    path('updateexpenses/<str:pk>/', views.updateexpenses, name='updateexpenses'),
    path('addincome/', views.addincome, name='addincome'),
    path('listincome/', views.listincome, name='listincome'),
    path('invoice/', views.invoice, name='invoice'),
]