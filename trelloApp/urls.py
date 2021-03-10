from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('creat_list/', views.creat_list, name='creat_list'),
    path('creat_task/', views.creat_task, name='creat_task'),
]