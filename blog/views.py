from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Post
from .forms import PostCreateForm

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
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_posts')
    else:
        form = PostCreateForm()

    return render(request, 'blog/create_post.html', context={'form':form})


def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostCreateForm(request.POST or None, instance = post)

    if form.is_valid():
        form.save()
        return redirect('all_posts')

    context = {
        'form': form,
    }

    return render(request, 'blog/update_post.html', context=context)

def remove_post(request, post_id):
    Post.objects.filter(id=post_id).delete()
    return redirect('all_posts')
















# def create_post(request):
    # if request.method == 'GET':
    #     return render(request, 'blog/create_post.html')
    # else request.method == 'POST':
        
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     user = User.objects.all()[0]
    #     Post.objects.create(title = post_title, text = post_text, status = 'pub', author = user)

    #     return render(request, 'blog/create_post.html')