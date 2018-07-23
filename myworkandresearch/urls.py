from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'myworkandresearch'
urlpatterns = [
    url(r'^$', views.myworkandresearch, name='myworkandresearch'),
    url(r'^(?P<category_slug>[\w-]+)/$', views.category, name='category'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<subject_slug>[\w-]+)/$', views.subject, name='subject'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<subject_slug>[\w-]+)/(?P<article_slug>[\w-]+)/$', views.detail, name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #upluad edicek dosyaların url'ini ayarladık