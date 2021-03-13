from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

def index(request):
    boards = List_board.objects.all()
    return render(request, 'workingAppTemplates/index.html', {'boards':boards})

def create_list_form(request, board_id):
    # get data from form and assign it
    if request.method == 'POST':
        form = Task_list_form(data= request.POST)
        # name = request.POST['name']
        # if form.is_valid():
        form.save()
        return redirect('board_descr', board_id)
    else:
        # FIXME:
        form = Task_list_form(initial= {'board_key': board_id})
        return render(request,'workingAppTemplates/formsTemplate/createList.html',{'form_data': form} )


def create_task_form(request, list_id):
    # get data from form and assign it
    if request.method == 'POST':
        form = Task_form(data=request.POST)
        name = request.POST['name']
        if form.is_valid():
            form.save()
            return redirect('list_descr', list_id)
    else:
        # FIXME:
        form = Task_form(initial= {'list_key': list_id})
        return render(request,'workingAppTemplates/formsTemplate/createTask.html', {'form_data':form})



def board_descr(request, board_id):
    boards = List_board.objects.filter(id=board_id)
    lists = Task_list.objects.filter(board_key= board_id )
    return render(request, 'workingAppTemplates/boards.html', {'lists': lists, 'board_name': boards[0].name, 'board_id': boards[0].id})
    # FIXME: why is it taking like boards[0].name 
    

def list_descr(request, list_id):
    lists = Task_list.objects.filter(id=list_id)
    tasks = Task.objects.filter(list_key=list_id)
    return render(request, 'workingAppTemplates/lists.html', {'tasks': tasks, 'list_name': lists[0].name, 'list_id': lists[0].id})