from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template import loader, context
from django.urls import reverse
from .models import Topic, Post


# Create your views here.
def blog(request):
    topics = Topic.objects.all()
    posts = Post.objects.all()
    context={
        'topics': topics,
        'posts':posts,
    }
    return render(request, 'blog/blog.html', context)

def topic(request,topic_slug):
    topic= Topic.objects.filter(slug=topic_slug)
    posts=Post.objects.all()
    post = get_object_or_404(Post, slug=post_slug)
    topics=Post.objects.all()
    context = {
        'topics': topics,
        'topic':topic,
        'posts':posts,
        'post':post
    }
    return render(request, 'blog/topic.html', context)



def post(request,topic_slug,post_slug):
    topic = Topic.objects.filter(slug=topic_slug)
    post= get_object_or_404(Post, slug=post_slug)
    context = {
        'topic': topic,
        'post': post
    }
    return render(request, 'blog/post.html', context)