# Create your views here.
from django.shortcuts import render, get_object_or_404,Http404
from django.template import loader, context
from django.urls import reverse
from .models import Topic, Post
from django.utils.text import slugify
from django.contrib.auth.models import User
from .forms import PostCommentForm #forms.py'deki Formları (CommentForm) aktarıyoruz:
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #sayfalama için gerekli kütüphaneleri aktarıyoruz:

#blog uygulaması Anasayfası (blog.html):
def blog(request):
    topic_list = Topic.objects.all()
    post_list = Post.objects.all()
    post_last=Post.objects.last()
    post_last_three=post_list.reverse()[1:4]
    post_six = post_list.reverse()[0]
    post_five=post_list.reverse()[1]
    post_four = post_list.reverse()[2]
    post_three = post_list.reverse()[3]
    post_two = post_list.reverse()[4]
    post_one = post_list.reverse()[5]


    #Blog Sayfalama sistemi 1.0:
    paginator = Paginator(post_list, 5)  # Sayfa başına 5 post göster
    page = request.GET.get('sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts= paginator.page(paginator.num_pages)

    context={
        'topic_list': topic_list,
        'post_list':post_list,
        'post_last':post_last,
        'post_last_three':post_last_three,
        'post_six':post_six,
        'post_five': post_five,
        'post_four': post_four,
        'post_three': post_three,
        'post_two': post_two,
        'post_one': post_one,
    }
    return render(request, 'blog/blog.html', context)

#blog uygulaması konulara ait postları içeren sayfa(topic.html):
def topic(request,topic_slug):
    topics= Topic.objects.filter(slug=topic_slug)
    topic_list=Topic.objects.all()
    posts = Post.objects.all()
    topic = get_object_or_404(Topic, slug=topic_slug)


    paginator = Paginator(posts, 5)  # Sayfa başına 5 post göster
    page = request.GET.get('sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        'topics': topics,
        'topic':topic,
        'topic_list':topic_list,
        'posts':posts,

    }
    return render(request, 'blog/topic.html', context)

#blog sayfası Post detaylarının olduğu sayfa (post.html):
def post(request,topic_slug,post_slug):
    topic = Topic.objects.filter(slug=topic_slug)
    related=topic[0:3]
    topic_list = Topic.objects.all()
    post= get_object_or_404(Post, slug=post_slug)

    # Post Yorum Sistemi 3.0 --> 4.0 için comment.html sayfasına git
    form = PostCommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    context = {
        'topic': topic,
        'related':related,
        'topic_list':topic_list,
        'post': post,
        'form' : form,
    }
    return render(request, 'blog/post.html', context)