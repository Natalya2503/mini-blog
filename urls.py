from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostHome.as_view(), name = 'home'),
    path('add_post/', views.add_post, name = 'add_post'),
    path('edit_post/<int:id>', views.edit_post, name = 'edit_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('show_post/<int:id>', views.ShowPost.as_view(), name='show_post')
]