from django.shortcuts import render,redirect
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .forms import CustomAuthenticationForm



# Create your views here.
def loginpage(request):
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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page after successful registration
            return redirect('loginpage')  # Replace 'success_page' with the URL name of your success page
    else:
        form = CustomUserCreationForm()

    # Render the registration form template with the form, even if it's not valid
    return render(request, 'registerpage.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')