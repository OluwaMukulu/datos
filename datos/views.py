from django.shortcuts import render,redirect
from .models import *
from .forms import CreateUserForm


# Create your views here.
def loginpage(request):

    context={}

    return render(request, 'loginpage.html', context)

def registerpage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}

    return render(request, 'registerpage.html', context)

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')