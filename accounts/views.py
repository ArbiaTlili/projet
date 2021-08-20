from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
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
        permission_required = 'catalog.can_mark_returned'
        return render(request, 'page1.html')
        permission_required = 'catalog.can_mark_returned'
        return render(request, 'page2.html')
    return redirect('/accounts/login')
   