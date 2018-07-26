from django.conf.urls import url
from . import views

app_name = 'hakkimda'
urlpatterns = [
    url(r'^$', views.hakkimda, name='hakkimda'),
]