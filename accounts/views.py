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



def home(request):
    if request.user.is_authenticated:
        logger.error(request.user)
        permission_required = 'assurance.can_add_souscriptiondecredit','assurance.can_edit_souscriptiondecredit','assurance.can_add_souscriptiondevoyage','assurance.can_edit_souscriptiondevoyage','assurance.can_delete_souscriptiondevoyage'
        return render(request, 'base3.html')
        permission_required = 'assurance.can_edit_assureur', 'assurance.can_add_assureur','assurance.can_add_baremedecredit','assurance.can_edit_baremedecredit','assurance.can_add_baremedevoyage','assurance.can_edit_baremedevoyage','assurance.can_add_produitassurance','assurance.can_edit_produitassurance','assurance.can_delete_produitassurance'
        return render(request, 'base1.html')
    
    return redirect('/accounts/login')
   