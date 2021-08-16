
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render, redirect  

from assurance.forms import ProduitassuranceForm  
from assurance.models import Produitassurance  
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def base2(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'base2.html', context)

def utilisateurs(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/utilisateurs.html', context)

def groupe(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/groupe.html', context)

def droits(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/droits.html', context)

def privilège(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/privilège.html', context)

def compte(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/compte.html', context)

def base3(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'base3.html', context)

def sousvoyage(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/sousvoyage.html', context)

def souscrédit(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/souscrédit.html', context) 

def compte1(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/compte1.html', context)       

def base1(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'base1.html',context)

def compagnies(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/compagnies.html', context)

def produit(request):
    context = {
        'welcome_text':"welcomecompte",
         
        "first_name": "test nom ",
        "last_name": "test prenom",
        "address": "test adresse"
    
    }
    return render(request, 'assurance/produit.html', context) 

def barémescrédit(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/barémescrédit.html', context)  

def barémesvoyage(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/barémesvoyage.html', context) 

def décision(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/décision.html', context)
     
def compte2(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/compte2.html', context)  

def ajt_user(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/utilisateurs.html', context)
# -----------------------------produitAssurance-----------------------------------
def produitAssurance(request):  
   
    if request.method == "POST":  
        form = ProduitassuranceForm(request.POST)  
        logger.error("sssssssssssss")
        logger.error(form.errors.as_data())
        logger.error(form.is_valid())
        if form.is_valid():
            try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                
                return redirect('produitAssurance/show')  
            except Exception as e:  
                logger.error( str( e))  
    else:  
        logger.error("else")
        form = ProduitassuranceForm()  
    return render(request,'produitAssurance/index.html',{'form':form})  
def showPA(request):  
    Produitassurances = Produitassurance.objects.all()  
    return render(request,"produitAssurance/show.html",{'Produitassurances':Produitassurances})  
def editPA(request, id):  
    Produitassurance1 = Produitassurance.objects.get(code_produit=id)  
    return render(request,'produitAssurance/edit.html', {'Produitassurance':Produitassurance1})  
def updatePA(request, id):  
    Produitassurance1 = Produitassurance.objects.get(code_produit=id)  
    form = ProduitassuranceForm(request.POST, instance = Produitassurance1)  
    if form.is_valid():
        try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                
                return redirect('produitAssurance/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'produitAssurance/edit.html', {'Produitassurance': Produitassurance1})  
def destroyPA(request, id):  
    Produitassurance = Produitassurance.objects.get(code_produit=id)  
    Produitassurance.delete()  
    return redirect("produitAssurance/show")