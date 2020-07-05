from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    blog_dict = {'content':"Hello now I am coming from blog/index.html!"}
    return render(request,"blog/index.html",context = blog_dict)