from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'userPagesTemplates/signup.html')
    
def sigin(request):
    # pass
    return render(request, 'userPagesTemplates/signin.html')
