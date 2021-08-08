from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def LoginPage(request):
    return render(request, 'login.html')

def HomePage(request):
    return render(request, 'home.html')


