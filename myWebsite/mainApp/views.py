from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    my_dict = {'content':"Hello now I am coming from mainApp/index.html!"}
    return render(request,"mainApp/index.html",context = my_dict)

def help(request):
    help_dict = {'content':"Hello now I am coming from mainApp/help.html!"}
    return render(request,"mainApp/help.html",context = help_dict)
