from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm





class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    extra_context = {'form': form_class}
    

    def get_success_url(self):
        return reverse_lazy('home')
