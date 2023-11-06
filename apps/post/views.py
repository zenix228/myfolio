from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required

from .forms import *

def home(request):
    return render(request, 'base.html')

def post(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(
        request,
        'post.html',
        context
    )


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='post')
    else: 
        form = PostForm()

    #print(ProductForm(request.POST).is_valid())
    context = {
        'form': form
    }
    return render(request, 'create_post.html', context)

def about(request):
    return render(request, 'about.html')