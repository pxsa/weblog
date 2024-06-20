from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Post

# Create your views here.
def say_hi(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def all(request):
    all_posts = Post.objects.filter(status='pub')
    return render(request, 'blog/posts.html', {'posts': all_posts})

def detail(request, post_id):
    # post = Post.objects.get(id = post_id)
    post = get_object_or_404(Post, pk=post_id)
    if post is None:
        return HttpResponse("page not founded", status=401 )
    return render(request, 'blog/detail.html', {'post': post})


def create_post(request):
    if request.method == 'GET':
        return render(request, 'blog/create_post.html')
    elif request.method == 'POST':
        
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')
        user = User.objects.all()[0]
        Post.objects.create(title = post_title, text = post_text, status = 'pub', author = user)

        return render(request, 'blog/create_post.html')