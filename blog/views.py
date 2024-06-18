from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

# Create your views here.
def say_hi(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def all(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': all_posts})

def detail(request, post_id):
    # post = Post.objects.get(id = post_id)
    post = get_object_or_404(Post, pk=post_id)
    if post is None:
        return HttpResponse("page not founded", status=401 )
    return render(request, 'blog/detail.html', {'post': post})