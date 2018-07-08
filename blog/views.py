from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template import loader, context
from django.urls import reverse
from .models import Category, Subject, Post


# Create your views here.
def blog(request):
    categories = Category.objects.all()
    subjects = Subject.objects.all()
    context={
        'categories': categories,

        'subjects':subjects,
    }
    return render(request, 'blog/blog.html', context)

def category(request,category_slug):
    categories= Category.objects.filter(slug=category_slug)
    subjects=Subject.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    posts=Post.objects.all()
    context = {
        'categories': categories,
        'category':category,
        'subjects':subjects,
        'Posts':posts
    }
    return render(request, 'blog/category.html', context)

def subject(request,category_slug,subject_slug):
    categories = Category.objects.filter(slug=category_slug)
    subjects = Subject.objects.all()
    subject = get_object_or_404(Subject, slug=subject_slug)
    posts = Post.objects.all()
    context = {
        'categories': categories,
        'subjects': subjects,
        'subject':subject,
        'posts': posts
    }
    return render(request, 'blog/subject.html', context)

def detail(request,category_slug,subject_slug,Post_slug):
    categories = Category.objects.filter(slug=category_slug)
    subjects = Subject.objects.filter(slug=subject_slug)
    posts = get_object_or_404(Post, slug=Post_slug)
    context = {
        'categories': categories,
        'subjects': subjects,
        'posts': posts
    }
    return render(request, 'blog/detail.html', context)