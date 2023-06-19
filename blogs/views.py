from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Post, Category


# Create your views here.

def about(request):
    cats = Category.objects.all()
    return render(request, 'about.html', {'cats': cats})


def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]

    cats = Category.objects.all()
    # print posts
    data = {
        'posts': posts,
        'cats': cats,
    }
    return render(request, 'home.html', data)


# if we want to send some data to view to the template then we pass it inside {}

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, 'category.html', {'cat': cat, 'posts': posts})
