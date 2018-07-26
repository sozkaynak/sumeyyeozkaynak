
# Create your views here.
from django.shortcuts import render, get_object_or_404,Http404, HttpResponseRedirect
from django.template import loader, context
from django.urls import reverse
from .models import Category, Subject, Article
from django.utils.text import slugify
from django.contrib.auth.models import User
from .forms import ArticleCommentForm, SubjectCommentForm, CategoryCommentForm #CommentForm'u import ettik

#Blog Sayfalama sistemi 1.0:
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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

    # Category Yorum Sistemi 3.0 --> 4.0 için comment.html sayfasına git
    form = CategoryCommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.subject = subject
        comment.save()


    context = {
        'categories': categories,
        'category':category,
        'subjects':subjects,
        'articles':articles,
        'form': form,
    }
    return render(request, 'myworkandresearch/category.html', context)

def subject(request,category_slug,subject_slug):
    categories = Category.objects.filter(slug=category_slug)
    subjects = Subject.objects.all()
    subject = get_object_or_404(Subject, slug=subject_slug)
    articles = Article.objects.all()

    # Subject Yorum Sistemi 3.0 --> 4.0 için comment.html sayfasına git
    form = SubjectCommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.subject = subject
        comment.save()


    context = {
        'categories': categories,
        'subjects': subjects,
        'subject':subject,
        'articles': articles,
        'form': form,
    }
    return render(request, 'myworkandresearch/subject.html', context)

def detail(request,category_slug,subject_slug,article_slug):
    categories = Category.objects.filter(slug=category_slug)
    subjects = Subject.objects.filter(slug=subject_slug)
    article = get_object_or_404(Article, slug=article_slug)

    # Article Yorum Sistemi 3.0 --> 4.0 için comment.html sayfasına git
    form = ArticleCommentForm(request.POST or None)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.article=article
        comment.save()


    context = {
        'categories': categories,
        'subjects': subjects,
        'article': article,
        'form' : form,
    }
    return render(request, 'myworkandresearch/detail.html', context)