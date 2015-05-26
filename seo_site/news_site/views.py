from django.http import HttpResponse
from django.core.context_processors import request
from django.template import RequestContext, loader
from .models import Article
from aptsources.distinfo import Template

def index(request):
    template = loader.get_template('news/index.html');
    articles = Article.objects.order_by('-public_date');
    context = RequestContext(request, {
    'articles' : articles
    })
    return HttpResponse(template.render(context));