from django.shortcuts import render
from myapp.models import *
from myapp.forms import *
# Create your views here.
def good (request) :
    return render(request,"contact.html")

def need (request) :
    return render(request,"FAQ.html")

def blog (request) :
    blg=blogs.objects.all()
    context={'blg':blg}
    return render(request,"blog.html",context)

def page (request) :
    return render(request,"page404.html") 

def works (request) :
    return render (request,"Restaurants.html")
    
def register (request) :
        return render (request,"register.html")

def hello (request) :
    blg=blogs.objects.all()[0:3 ]
    context={'blg':blg}
    return render(request,"fws.html",context)
      

def orderss(request) :
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'register.html')




def feedback(request):
    if request.method=="POST":
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'contact.html')