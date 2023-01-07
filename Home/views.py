from django.shortcuts import render,HttpResponse
from Home.models import Share
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def code(request):
    return render(request, 'code.html')

def needcode(request):
    return render(request, 'needcode.html')
def c(request):
    return render(request, 'CodeIde/c.html')
def cpp(request):
    return render(request, 'CodeIde/c++.html')
def java(request):
    return render(request, 'CodeIde/java.html')
def python(request):
    return render(request, 'CodeIde/python.html')
def js(request):
    return render(request, 'CodeIde/javascript.html')
def sql(request):
    return render(request, 'CodeIde/sql.html')

def share(request):
    if request.method=="POST":
        program = request.POST.get('program')
        language = request.POST.get('language')
        code = request.POST.get('code')
        share = Share(program=program,language=language,code=code)
        share.save()
        messages.success(request, 'Thanks For Helping!')
        
    return render(request, 'share.html')

