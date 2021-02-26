from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib import messages



'''def home_user (request):
    context = {}
    query= ""
    if request.GET:
        query = request.GET['querise']
        context['query'] = str(query) 
    return render(request,'wscrp/index.html',context)'''

def register(request):
    form = UserCreationForm()
    return render(request, 'user/register.html',{'title': 'Create account',
    'form': form})
