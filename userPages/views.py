from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from workingApp.views import index
from .forms import *
from workingApp.forms import *
from workingApp.models import *

# this dashboard is renamed from index and cut from the workingApp/ views.py 
@login_required(login_url='signin')
def dashboard(request): 
    # boards = List_board.objects.all()
    user = request.user
    list = Task_list.objects.filter(user_key = user) 
    return render(request, 'workingAppTemplates/dashboard.html', {'lists':list})

def index(request): # used for a new comer for login/signup or to reaad about our app
    return render(request, 'userPagesTemplates/index.html')
def signup(request):
    if request.method == 'POST':
        # form = UserCreationForm(data= request.POST)
        form = signupForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:   
        # form = UserCreationForm()
        form = signupForm()
    return render(request, 'userPagesTemplates/signup.html', {'form_data':form})
#  in case of is_valid()== false this should return to the same page of signup thats why we are returning outside the else.


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # user exists :: ?
        user = authenticate(request, username=username, password= password )
        if user is not None:
        # login
            login(request, user)
            return redirect('dashboard')
        else:
            # showing message on invalid credentials
            messages.error(request, "invalid login details")
    return render(request, 'userPagesTemplates/signin.html')

def signout(request):
    logout(request)
    return redirect('index')
