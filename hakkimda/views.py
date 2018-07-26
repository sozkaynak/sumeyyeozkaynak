# Create your views here.
from django.shortcuts import render, get_object_or_404,Http404
from django.template import loader, context
from django.urls import reverse
from .models import Hakkimda
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #sayfalama için gerekli kütüphaneleri aktarıyoruz:


def hakkimda(request): #request yerine herhangi bir şeyde yazabilirsiniz. Fakat genel olarak böyle adlandırılır.

    hakkimda=Hakkimda.objects.all()
    context = {
        'hakkimda':hakkimda,
    }

    return render(request,"hakkimda.html", context)