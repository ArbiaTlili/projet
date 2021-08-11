from django.shortcuts import render
from django.http import HttpResponse
from .form import Utilisateur
# Create your views here.
def index(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/index.html', context)

def utilisateurs(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    util = Utilisateur()  
    return render(request, 'assurance/utilisateurs.html', context,{'form':util})

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

def index1(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/index1.html', context)

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

def index2(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/index2.html',context)

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

