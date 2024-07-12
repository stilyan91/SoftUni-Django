from django.shortcuts import render

from cbv_demos.web.models import Articles


#View in Django:
#1. The view must be 'callable'
#2. Return HttpResponse object


def list_view(request):
    article = Articles.objects.all()
    context = {'articles': article}
    return render(request, 'articles.list.html', context)
