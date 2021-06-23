from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def show(request, slug):
    return HttpResponse("news slug is: %s." % slug)

def categories(request):
    return HttpResponse("news categories." )

def category(request, slug):
    return HttpResponse("news categories slug: %s." % slug)
