from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label = 'Логин',
                             widget= forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(max_length=50, label = 'Пароль',
                               widget= forms.PasswordInput(attrs={'class':'form-input'}))
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']