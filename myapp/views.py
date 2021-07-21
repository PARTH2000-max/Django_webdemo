from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    """context = {
        "variable":"herry is great",
        "variable1":"parth is great"
    }"""
   #messages.success(request,"This is test message")
    #return HttpResponse("this is our home page")
    return render(request ,'index.html')

def about(request):
    #return HttpResponse("this is about page")
    return render(request ,'about.html')       

def services(request):
    #return HttpResponse("this is service page")
    return render(request ,'services.html')    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact = Contact(name= name,email= email ,phone = phone ,desc=desc,date = datetime.today())
        contact.save()
        messages.success(request, 'Your message Has been sent!')
    #return HttpResponse("this is contact page")    
    return render(request ,'contact.html')