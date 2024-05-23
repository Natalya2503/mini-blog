from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm




def logout_user(request):
    return HttpResponse('logout')

class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    extra_context = {'form': form_class}
    

    def get_success_url(self):
        return reverse_lazy('home')