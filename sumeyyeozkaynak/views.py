
from django.shortcuts import render


def index(request): #request yerine herhangi bir şeyde yazabilirsiniz. Fakat genel olarak böyle adlandırılır.

    context = {

    }

    return render(request,"index.html", context)

def hakkimda(request): #request yerine herhangi bir şeyde yazabilirsiniz. Fakat genel olarak böyle adlandırılır.

    context = {

    }

    return render(request,"hakkimda.html", context)