from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('logout/', views.LogoutUser.as_view(), name='logout')
    
]

app_name = 'users'