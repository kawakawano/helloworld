from django.http import HttpResponse
from django.views.generic import TemplateView

def somebiew(request):
    print(Path(__file__).resolve().parent.parent)
    return HttpResponse('')

def helloworldfunction(request):
    returnobject = HttpResponse('<h1>hello world</h1>')
    return returnobject

class HellowWrldClass(TemplateView):
    template_name = 'hello.html'
