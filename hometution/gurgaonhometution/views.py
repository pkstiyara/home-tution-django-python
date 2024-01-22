from django.shortcuts import render

# Create your views here.


def register(request):
    # Handle registration logic
    return render(request, 'register.html')

def login_user(request):
    # Handle login logic
    return render(request, 'login.html')

def dashboard(request):
    # Handle dashboard logic
    return render(request, 'dashboard.html')
