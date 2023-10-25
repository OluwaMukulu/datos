from django.shortcuts import render,redirect
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .forms import CustomAuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                # Redirect to a success page after successful login
                return redirect('dashboard')  # Replace 'success_page' with the URL name of your success page
        else:
            form = CustomAuthenticationForm()

    # Render the login form template with the form
    return render(request, 'loginpage.html', {'form': form})

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                    form.save()
                    # Redirect to a success page after successful registration
                    return redirect('loginpage')  # Replace 'success_page' with the URL name of your success page
    

        # Render the registration form template with the form, even if it's not valid
        return render(request, 'registerpage.html', {'form': form})


def logoutpage(request):
    logout(request)
    return redirect('loginpage')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='loginpage')
def dashboard(request):
    context = {}
    if request.user.is_authenticated:
        context['first_name'] = request.user.first_name
    return render(request, 'dashboard.html', context)

@login_required(login_url='loginpage')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='loginpage')
def listexpenses(request):
    return render(request, 'listexpenses.html')

@login_required(login_url='loginpage')
def addexpenses(request):
    return render(request, 'addexpenses.html')

@login_required(login_url='loginpage')
def listincome(request):
    return render(request, 'listincome.html')

@login_required(login_url='loginpage')
def addincome(request):
    return render(request, 'addincome.html')

@login_required(login_url='loginpage')
def invoice(request):
    return render(request, 'invoice.html')