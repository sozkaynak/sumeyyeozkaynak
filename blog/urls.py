from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^(?P<topic_slug>[\w-]+)/$', views.topic, name='topic'),
    url(r'^(?P<topic_slug>[\w-]+)/(?P<post_slug>[\w-]+)/$', views.post, name='post'),
]
