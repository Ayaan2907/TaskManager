
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('dashboard', dashboard.as_view(), name='dashboard'), #show all lists
    # path('dashboard', dashboard, name='dashboard'), #show all lists
    path('list/<int:listId>', list_descr, name= 'list_descr'),     #show tasks in a list
    path('createlist/', createList.as_view(), name= 'create_list_form'),     #shows form for adding list inside a specific board
    path('createtask/<int:listId>', createTask.as_view(), name= 'create_task_form'),     #shows form for adding task inside a specific list


]

