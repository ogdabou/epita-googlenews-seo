from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import request
from django.template import RequestContext, loader
from .models import Article
from django.shortcuts import render
from .forms import RequestForm
from aptsources.distinfo import Template

from .JsonLoader import JsonLoader

# Create your views here.

def index(request):
    template = loader.get_template('news/index.html');
    articles = Article.objects.order_by('-public_date');
    context = RequestContext(request, {
    'articles' : articles
    })
    return HttpResponse(template.render(context));



def addRss (request):
    template = loader.get_template('admin/add/rss.html')
    jsonLoader = JsonLoader()
    datas = jsonLoader.load()
    articles = jsonLoader.transform(datas)
    context = RequestContext(request, {
        'articles' : articles
    })
    return HttpResponse(template.render(context))

