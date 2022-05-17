from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def help(request):
    my_dict = {'insert_me': "Help page from view.py!"}
    return render(request, 'help.html', context= my_dict)
