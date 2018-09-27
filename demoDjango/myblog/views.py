from django.shortcuts import render

# Create your views here.
def hello(request):
    context = {}
    context['hello'] = 'test hello world'
    return render(request,'hello.html',context)


def index(request):
    context = {}
    context['ip']= getIP(request)
    return render(request,'index.html',context)


def getIP(request):
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip