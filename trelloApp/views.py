from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

lists = Lists.objects.all()  
Task = Task.objects.all()

def index(request):
    return HttpResponse("Hello")

def home(request):
    return render(request, "trelloAppTemplates/home.html")

def model(request):
    if request.method == 'POST':
        list_title = request.POST['title']
        list_note = request.POST['note']
        list_vars = Lists(title = list_title, note= list_note)
        list_vars.save()
        return redirect('model')
    else:
        return render(request, "trelloAppTemplates/lists.html", {'Lists': lists })
################################
#
#   SEE THE CURRENT COMMIT MWAAAGE
#
################################
