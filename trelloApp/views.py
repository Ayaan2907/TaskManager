from django.shortcuts import render
from django.http import HttpResponse

# home= {'dic1':'dic', 'dic2':'dic2'}
def index(request):
    return HttpResponse("Hello")

def home(request):
    return render(request, "trelloAppTemplates/home.html",{'home': 1234567890})