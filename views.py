from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect, HttpResponseNotFound

def index(request):
    results = Post.objects.all()
    data = {
        'posts': results,

    }

    return render(request, 'index.html', data)

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


def show_post(request, id):
    show = Post.objects.get(id=id)
    data = {
        'title': show.title,
        'content': show.content,
        'author': show.author,
        'time_create': show.time_create

    }
    return render(request, 'show_post.html', data)