from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import TemplateView, ListView, DetailView

# def index(request):
#     results = Post.objects.all()
#     data = {
#         'posts': results,

#     }

#     return render(request, 'index.html', data)

# class PostHome(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = Post.objects.all()
#         return context

class PostHome(ListView):
    template_name = 'index.html'
    context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 
    def get_queryset(self):
        return Post.objects.all()

class ShowPost(DetailView):
    model = Post
    template_name = 'show_post.html'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        show = Post.objects.get(id=self.kwargs['id'])
        context = super().get_context_data(**kwargs)
        context['title']= show.title
        context['content']= show.content
        context['author']= show.author
        context['time_create']= show.time_create
        return context
    
    


    



# представление для формы не связанной с моделью
# def add_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             try:
#                 Post.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
           
#             return redirect('home')
#     else:
#       form = PostForm()
   
#     data = {
#         'form': form
#     }
#     return render(request, 'add_post.html', data)

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
      form = PostForm()
   
    data = {
        'form': form
    }
    return render(request, 'add_post.html', data)

def edit_post(request, id):
      try:
        post = Post.objects.get(id=id)
 
        if request.method == "POST":
            post.title = request.POST.get("title")
            post.content = request.POST.get("content")
            post.author = request.POST.get('author')

            post.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_post.html", {'form': PostForm()})
      except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Такой пост не был найден</h2>")
  
    
def delete_post(request, id):
    try:
        Post.objects.get(id=id).delete()
        return HttpResponseRedirect('/')
    except Post.DoesNotExist:
        return HttpResponseNotFound('<h2>Такой пост не был найден</h2>')


# def show_post(request, id):
#     show = Post.objects.get(id=id)
#     data = {
#         'title': show.title,
#         'content': show.content,
#         'author': show.author,
#         'time_create': show.time_create

#     }
#     return render(request, 'show_post.html', data)