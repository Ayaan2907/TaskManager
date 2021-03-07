from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

Lists = Lists.objects.all()  
Task = Task.objects.all()

def index(request):
    return HttpResponse("Hello")

def home(request):
    return render(request, "trelloAppTemplates/home.html")

def model(request):
    return render(request, "trelloAppTemplates/lists.html", {'Lists': Lists })

