
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #show all boards

    path('board/<int:board_id>', views.board_descr, name= 'board_descr'),     #show lists in a board
    path('list/<int:list_id>', views.list_descr, name= 'list_descr'),     #show tasks in a list
    path('creatlist/<int:board_id>', views.create_list_form, name= 'create_list_form'),     #shows form for adding list inside a specific board
    path('createtask/<int:list_id>', views.create_task_form, name= 'create_task_form'),     #shows form for adding task inside a specific list


]

