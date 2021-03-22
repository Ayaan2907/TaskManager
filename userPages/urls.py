from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('dashboard', views.dashboard, name='dashboard'), #show all lists
    path('signup', views.signup, name= 'signup' ),
    path('signin', views.signin, name= 'signin' ),
    path('signout', views.signout, name='signout'),
]
