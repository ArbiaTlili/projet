
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render, redirect  
from django.contrib import messages
from assurance.forms import ProduitassuranceForm ,AssureurForm 
from assurance.models import Produitassurance ,Assureur
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
               
                myform=form.save()  
                messages.success(request,"produit ajouter avec success")
                return redirect('/assurance/produitAssurance/show')  
            except Exception as e:  
                logger.error( str( e))  
    else:  
        messages.error(request,"verifier tous les champs")
        form = ProduitassuranceForm()  
    return render(request,'produitAssurance/index.html',{'form':form})  
def showPA(request): 

    if request.method == 'GET': # If the form is submitted
        
        search_query = request.GET.get('search_box', None)
        logger.error(search_query)
        # Do whatever you need with the word the user looked for

    # Your code
    Produitassurances = Produitassurance.objects.all()  
    return render(request,"produitAssurance/show.html",{'Produitassurances':Produitassurances})  
def editPA(request, id):  
    Produitassurance1 = Produitassurance.objects.get(code_produit=id)  
    return render(request,'produitAssurance/edit.html', {'Produitassurance':Produitassurance1})  
def updatePA(request, id):  
    Produitassurance1 = Produitassurance.objects.get(code_produit=id)  
    form = ProduitassuranceForm(request.POST, instance = Produitassurance1)  
    logger.error(form.errors.as_data())
    if form.is_valid():
        try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                
                return redirect('/assurance/produitAssurance/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'produitAssurance/edit.html', {'Produitassurance': Produitassurance1})  
def destroyPA(request, id):  
    Produitassurance1 = Produitassurance.objects.get(code_produit=id)  
    Produitassurance1.delete()  
    return redirect("/assurance/produitAssurance/show")



    # -----------------------------Assureur-----------------------------------
def Assureurindex(request):  
   
    if request.method == "POST":  
        form = AssureurForm(request.POST)  
        logger.error("sssssssssssss")
        logger.error(form.errors.as_data())
     
        if form.is_valid():
            try:  
               
                myform=form.save()  
                messages.success(request,"Assureur ajouter avec success")
                return redirect('/assurance/Assureur/show')  
            except Exception as e:  
                logger.error( str( e))  
    else:  
        messages.error(request,"verifier tous les champs")
        form = AssureurForm()  
    return render(request,'Assureur/index.html',{'form':form})  
def showA(request): 

   
    # Your code
    Assureurs = Assureur.objects.all()  
    return render(request,"Assureur/show.html",{'Assureurs':Assureurs})  
def editA(request, id):  
    Assureur1 = Assureur.objects.get(code_assureur=id)  
    return render(request,'Assureur/edit.html', {'Assureur':Assureur1})  
def updateA(request, id):  
    Assureur1 = Assureur.objects.get(code_assureur=id)  
    form = AssureurForm(request.POST, instance = Assureur1)  
    
    if form.is_valid():
        try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                
                return redirect('/assurance/Assureur/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'Assureur/edit.html', {'Assureur': Assureur1})  
def destroyA(request, id):  
    instance = Assureur.objects.get(code_assureur=id)
    instance.delete() 
    return redirect("/assurance/Assureur/show")