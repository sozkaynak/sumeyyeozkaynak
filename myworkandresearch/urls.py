from django.conf.urls import url
from . import views

app_name = 'myworkandresearch'
urlpatterns = [
    url(r'^$', views.myworkandresearch, name='myworkandresearch'),
    url(r'^(?P<category_slug>[\w-]+)/$', views.category, name='category'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<subject_slug>[\w-]+)/$', views.subject, name='subject'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<subject_slug>[\w-]+)/(?P<article_slug>[\w-]+)/$', views.detail, name='detail'),
]
