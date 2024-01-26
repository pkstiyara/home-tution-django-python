from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is home page.")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about.")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services.")

def contact(request):
    return render(request, 'contact.html')
    
    #return HttpResponse("This is contactus.")