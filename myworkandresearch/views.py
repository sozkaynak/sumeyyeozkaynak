from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template import loader, context
from django.urls import reverse
from .models import Category, Subject, Article


# Create your views here.
def myworkandresearch(request):
    categories = Category.objects.all()
    subjects = Subject.objects.all()
    context={
        'categories': categories,

        'subjects':subjects,
    }
    return render(request, 'myworkandresearch/myworkandresearch.html', context)

def category(request,category_slug):
    categories= Category.objects.filter(slug=category_slug)
    subjects=Subject.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    articles=Article.objects.all()
    context = {
        'categories': categories,
        'category':category,
        'subjects':subjects,
        'articles':articles
    }
    return render(request, 'myworkandresearch/category.html', context)

def subject(request,category_slug,subject_slug):
    categories = Category.objects.filter(slug=category_slug)
    subjects = Subject.objects.all()
    subject = get_object_or_404(Subject, slug=subject_slug)
    articles = Article.objects.all()
    context = {
        'categories': categories,
        'subjects': subjects,
        'subject':subject,
        'articles': articles
    }
    return render(request, 'myworkandresearch/subject.html', context)

def detail(request,category_slug,subject_slug,article_slug):
    categories = Category.objects.filter(slug=category_slug)
    subjects = Subject.objects.filter(slug=subject_slug)
    articles = get_object_or_404(Article, slug=article_slug)
    context = {
        'categories': categories,
        'subjects': subjects,
        'articles': articles
    }
    return render(request, 'myworkandresearch/detail.html', context)