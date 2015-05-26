from django.http import HttpResponse

from .JsonLoader import JsonLoader


# Create your views here.

def index (request):
    jsonR = JsonLoader()
    datas = jsonR.load()
    jsonR.transform(datas)
    return HttpResponse("Hello world, this is index")