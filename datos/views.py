from django.shortcuts import render,redirect
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .forms import CustomAuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm
from .models import PAYMENT_METHOD
from django.db import transaction



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
    if request.user.is_authenticated:
        return redirect('dashboard')
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

    expense = Expense.objects.all()  # Assuming Expense is your model name
    context = {
        'expense': expense,
    }

    return render(request, 'listexpenses.html', context)

@login_required(login_url='loginpage')
def addexpenses(request):

    form = ExpenseForm()

    expense = Expense.objects.all()
    payment_methods = [method[0] for method in PAYMENT_METHOD]
    unique_categories = Expense.objects.values_list('category_name__category_name', flat=True).distinct()
    suppliers = Expense.objects.values_list('company_name__company_name', flat=True).distinct()

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            with transaction.atomic():
                form.save()
            return redirect('listexpenses')
        
    context = {'form':form,'expense': expense,'payment_methods':payment_methods,'unique_categories':unique_categories,'suppliers':suppliers}
    return render(request, 'addexpenses.html', context)

@login_required(login_url='loginpage')
def updateexpenses(request, pk):

    payment_methods = [method[0] for method in PAYMENT_METHOD]
    unique_categories = Expense.objects.values_list('category_name__category_name', flat=True).distinct()

    expense = Expense.objects.get(id=pk) 
    form = ExpenseForm(instance=expense)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('listexpenses')

    context = {'form':form,'payment_methods':payment_methods,'unique_categories':unique_categories}
    return render(request, 'updateexpenses.html', context)

@login_required(login_url='loginpage')
def listincome(request):
    return render(request, 'listincome.html')

@login_required(login_url='loginpage')
def addincome(request):
    return render(request, 'addincome.html')

@login_required(login_url='loginpage')
def invoice(request):
    return render(request, 'invoice.html')
