
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    # path('dashboard', dashboard, name='dashboard'), #show all lists
    path('dashboard', dashboard.as_view(), name='dashboard'), #show all lists
    path('uupdateList/<int:pk>', updateList.as_view(), name= 'update_list'),     #show tasks in a list
    path('list/<int:listId>', list_descr, name= 'list_descr'),     #show tasks in a list
    path('createlist/', createList.as_view(), name= 'create_list_form'),     #shows form for adding list inside a specific board
    path('deletelist/<int:pk>', DeleteList.as_view(), name= 'delete_list'), 
    # path('createtask/<int:listId>', createTask.as_view(), name= 'create_task_form'),     #shows form for adding task inside a specific list


]

