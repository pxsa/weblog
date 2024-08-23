from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
from django.views import generic

from .models import Post
from .forms import PostCreateForm


# def all(request):
#     all_posts = Post.objects.filter(status='pub')
#     return render(request, 'blog/posts.html', {'posts': all_posts})

class PostList(generic.ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-date_modified')

# def detail(request, post_id):
#     # post = Post.objects.get(id = post_id)
#     post = get_object_or_404(Post, pk=post_id)
#     if post is None:
#         return HttpResponse("page not founded", status=401 )
#     return render(request, 'blog/detail.html', {'post': post})

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_posts')
    else:
        form = PostCreateForm()

    return render(request, 'blog/create_post.html', context={'form':form})


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostCreateForm(request.POST or None, instance = post)

    if form.is_valid():
        form.save()
        return redirect('all_posts')

    context = {
        'form': form,
    }

    return render(request, 'blog/update_post.html', context=context)

def remove_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    Post.objects.filter(id=pk).delete()
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