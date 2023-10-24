from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User





class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'username', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
