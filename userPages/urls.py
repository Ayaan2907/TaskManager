from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', index, name= 'index'),
    path('dashboard', dashboard, name='dashboard'), #show all lists
    path('signup', signup, name= 'signup' ),
    path('signin', customeSignin.as_view(), name= 'signin' ),
    # path('signin', signin, name= 'signin' ),
    path('signout', signout, name='signout'),
]