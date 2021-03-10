from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import Task_form

lists = Lists.objects.all()  
task = Task.objects.all()

def index(request):
    return HttpResponse("Hello")

def home(request):
    return render(request, "trelloAppTemplates/home.html",  {'Lists': lists, 'Tasks': task })

def creat_list(request):
    if request.method == 'POST':
        list_title = request.POST['title']
        list_note = request.POST['note']
        list_vars = Lists(title = list_title, note= list_note)
        list_vars.save()
        return redirect('home') # this line will work after the form data is entered and submitted
    else:
        return render(request, "trelloAppTemplates/lists.html") # this page will display the form template to be filled

def creat_task(request):
    if request.method == 'POST':
        Form = Task_form(data=request.POST)
        # if Form.is_valid():
        Form.save()
        return redirect('home') # this line will work after the form data is entered and submitted
    else:
        Form = Task_form()
        return render(request, "trelloAppTemplates/tasks.html", {'form':Form}) # this page will display the form template to be filled
