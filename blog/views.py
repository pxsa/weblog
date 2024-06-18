from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def say_hi(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def all(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': all_posts})

def detail(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'blog/detail.html', {'post': post})