from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from blog.models import Article 
# from Article import published_date

# def home_page(request):
#     context = {
#         'name': 'Meke',
#         'current_time': datetime.now()
#     }
#     response = render(request, 'index.html', context)
#     return HttpResponse(response)

# def index(request):
#   return HttpResponseRedirect("/articles")

# def all(request):
#   articles = Article.objects.all()
#   context = {"articles": articles}
#   return render(request, 'all.html', context)

# def show(request, id):
#   article = Article.objects.get(pk=id)
#   context = {"article": article}
#   return render(request, 'show.html', context)

def root(request):
    return HttpResponseRedirect("index")

def index(request):
    article = Article.objects.all()
    # article = Article.objects.all().order_by(-published_date),
    # article = Article.objects.filter(published_date=2019).order_by('-published_date'),
    context = {
      'current_time': datetime.now(),
      "articles": article
    }
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def show(request, id):
    article = Article.objects.get(pk=id)
    context = {"article": article}
    return render(request, "show.html", context)
