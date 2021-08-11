from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
import logging



logger = logging.getLogger(__name__)
def logout(request):
    logout(request)
# Create your views here.
def LoginPage(request):
    return render(request, 'login.html')

def HomePage(request):
    return render(request, 'home.html')

def home(request):
    if request.user.is_authenticated:
        logger.error(request.user)
        return render(request, 'home.html')
    return redirect('/accounts/login')
   