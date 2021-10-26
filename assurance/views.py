
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render, redirect  
from django.contrib import messages
from assurance.forms import ProduitassuranceForm, ProduitcreditForm, AssureurForm, BaremeassurancevoyageForm, BaremeassurancecreditForm, SouscriptioncreditForm, SouscriptionvoyageForm, beneficiaireForm  
from assurance.models import Produitvoyage , Produitcredit, Assureur, Baremedevoyage, Baremedecredit, Souscriptiondecredit,  Souscriptiondevoyage, Beneficiaire
from django.contrib.auth.models import Permission
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def base2(request):
 
    return render(request, 'base2.html', context)


def base3(request):
 
    return render(request, 'base3.html')
  

def base1(request):
  
    return render(request, 'base1.html')


def home(request):
    perm_tuple = [( x.name) for x in Permission.objects.filter(user=request.user)]
    logger.error(perm_tuple)
    if request.user.is_authenticated:
        logger.error('Can add produitassurance' in perm_tuple)
        if 'Can add produitassurance' in perm_tuple:
            return render(request, 'base1.html')
        elif 'Can add souscriptiondecredit' in perm_tuple:
            return render(request, 'base3.html')
        # permission_required = 'assurance.can_add_souscriptiondecredit','assurance.can_edit_souscriptiondecredit','assurance.can_add_souscriptiondevoyage','assurance.can_edit_souscriptiondevoyage','assurance.can_delete_souscriptiondevoyage'
        
        # permission_required = 'assurance.can_edit_assureur', 'assurance.can_add_assureur','assurance.can_add_baremedecredit','assurance.can_edit_baremedecredit','assurance.can_add_baremedevoyage','assurance.can_edit_baremedevoyage','assurance.can_add_produitassurance','assurance.can_edit_produitassurance','assurance.can_delete_produitassurance'
        
    return redirect('/accounts/login')
 

def décision(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/décision.html', context)

    

def navbar(request):
      
    return render(request, 'navbar.html')  

def navbar1(request):
      
    return render(request, 'navbar1.html')          

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
            messages.warning(request,"verifier tous les champs")
    else:    
        form = ProduitassuranceForm()  
    return render(request,'produitAssurance/index.html',{'form':form})  
def showPA(request): 

    

    # Your code
    Produitvoyages = Produitvoyage.objects.all()  
    return render(request,"produitAssurance/show.html",{'Produitvoyages':Produitvoyages})  
def editPA(request, id):  
    Produitvoyage1 = Produitvoyage.objects.get(code_produit=id)  
    return render(request,'produitAssurance/edit.html', {'Produitvoyage':Produitvoyage1})  
def updatePA(request, id):  
    Produitvoyage1 = Produitvoyage.objects.get(code_produit=id)  
    form = ProduitassuranceForm(request.POST, instance = Produitvoyage1)  
    logger.error(form.errors.as_data())
    if form.is_valid():
        try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                messages.success(request, 'modification avec succès!')
                return redirect('/assurance/produitAssurance/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'produitAssurance/edit.html', {'Produitvoyage': Produitvoyage1})  
def destroyPA(request, id):  
    Produitvoyage1 = Produitvoyage.objects.get(code_produit=id)  
    Produitvoyage1.delete() 
    messages.warning(request, 'suppression avec succès!')
    return redirect("/assurance/produitAssurance/show")


def produitcredit(request):  
   
    if request.method == "POST":  
        form = ProduitcreditForm(request.POST)  
        logger.error("sssssssssssss")
        logger.error(form.errors.as_data())
        logger.error(form.is_valid())
        if form.is_valid():
            try:  
               
                myform=form.save()  
                messages.success(request,"produit ajouter avec success")
                return redirect('/assurance/produitcredit/show')  
            except Exception as e:  
                logger.error( str( e))  
        else:  
            messages.warning(request,"verifier tous les champs")
    else:    
        form = ProduitcreditForm()  
    return render(request,'produitcredit/index.html',{'form':form})  
def showPC(request): 

    

    # Your code
    Produitcredits = Produitcredit.objects.all()  
    return render(request,"produitcredit/show.html", {'Produitcredits':Produitcredits})  
def editPC(request, id):  
    Produitcredit1 = Produitcredit.objects.get(code_produitC=id)  
    return render(request,'produitcredit/edit.html', {'Produitcredit':Produitcredit1})  
def updatePC(request, id):  
    Produitcredit1 = Produitcredit.objects.get(code_produitC=id)  
    form = ProduitcreditForm(request.POST, instance = Produitcredit1)  
    logger.error(form.errors.as_data())
    if form.is_valid():
        try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                messages.success(request, 'modifiacation avec succés!')
                return redirect('/assurance/produitcredit/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'produitcredit/edit.html', {'Produitcredit': Produitcredit1})  
def destroyPC(request, id):  
    Produitcredit1 = Produitcredit.objects.get(code_produitC=id)  
    Produitcredit1.delete() 
    messages.warning(request, 'suppression avec succés!')
    return redirect("/assurance/produitcredit/show")

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
            messages.warning(request,"verifier tous les champs")
    else:    
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
                messages.success(request, 'modification avec succés!')
                return redirect('/assurance/Assureur/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'Assureur/edit.html', {'Assureur': Assureur1})  
def destroyA(request, id):  
    instance = Assureur.objects.get(code_assureur=id)
    instance.delete() 
    messages.warning(request, 'suppression avec succés!')
    return redirect("/assurance/Assureur/show")



    # -----------------------------Bareme assurance voyage-----------------------------------
def Baremevoyageindex(request):  
   
    if request.method == "POST":  
        form = BaremeassurancevoyageForm(request.POST)  
        logger.error("sssssssssssss")
        logger.error(form.errors.as_data())
     
        if form.is_valid():
            try:  
               
                myform=form.save()  
                messages.success(request,"Barème voyage ajouté avec success")
                return redirect('/assurance/Baremevoyage/show')  
            except Exception as e:  
                logger.error( str( e))  
        else:  
           messages.warning(request,"verifier tous les champs")
    else:    
        form = BaremeassurancevoyageForm()  
    return render(request,'Baremevoyage/index1.html',{'form':form})  
def showB(request): 

   
    # Your code
    Baremedevoyages = Baremedevoyage.objects.all()  
    return render(request,"Baremevoyage/show.html",{'Baremedevoyages':Baremedevoyages})  
def editB(request, id):  
    Baremedevoyage1 = Baremedevoyage.objects.get(id_bareme_voyage=id)  
    logger.error(Baremedevoyage1)
    return render(request,'Baremevoyage/edit.html', {'Baremedevoyage':Baremedevoyage1})  
def updateB(request, id):  
    Baremedevoyage1 = Baremedevoyage.objects.get(id_bareme_voyage=id)  
    form = BaremeassurancevoyageForm(request.POST, instance=Baremedevoyage1) 
  
    
    if request.method == "POST":
        logger.error(form.errors.as_data())           
        if form.is_valid():
            try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                messages.success(request, 'modification avec succès!')
                return redirect('/assurance/Baremevoyage/show')  
            except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'Baremevoyage/edit.html', {'Baremedevoyage': Baremedevoyage1})  
def destroyB(request, id):  
    instance = Baremedevoyage.objects.get(id_bareme_voyage=id)
    instance.delete()
    messages.warning(request, 'suppression avec succès!')
    return redirect("/assurance/Baremevoyage/show")

 # -----------------------------Bareme assurance credit-----------------------------------
def Baremecreditindex(request):  
    if request.method == "POST":  
        form = BaremeassurancecreditForm(request.POST)  
        logger.error("sssssssssssss")
        logger.error(form.errors.as_data())
     
        if form.is_valid():
            try:  
               
                myform=form.save()  
                messages.success(request,"Barème crédit ajouter avec success")
                return redirect('/assurance/Baremecredit/show')  
            except Exception as e:  
                logger.error( str( e))  
        else:  
            messages.warning(request,"verifier tous les champs")
    else:    
        form = BaremeassurancecreditForm()  
    return render(request,'Baremecredit/index2.html',{'form':form})  
def showC(request): 

   
    # Your code
    Baremedecredits = Baremedecredit.objects.all()  
    return render(request,"Baremecredit/show.html",{'Baremedecredits':Baremedecredits})  
def editC(request, id):  
    Baremedecredit1 = Baremedecredit.objects.get(id_bareme_credit=id)  
    return render(request,'Baremecredit/edit.html', {'Baremedecredit':Baremedecredit1})  
def updateC(request, id):  
    Baremedecredit1 = Baremedecredit.objects.get(id_bareme_credit=id)  
    form = BaremeassurancecreditForm(request.POST, instance = Baremedecredit1)  
    
    if form.is_valid():
        try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                messages.success(request, 'modification avec succès!')
                return redirect('/assurance/Baremecredit/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'Baremecredit/edit.html', {'Baremedecredit': Baremedecredit1})  
def destroyC(request, id):  
    instance = Baremedecredit.objects.get(id_bareme_credit=id)
    instance.delete() 
    messages.warning(request, 'suppression avec succès!')
    return redirect("/assurance/Baremecredit/show")


 # -----------------------------Souscription d'assurance credit-----------------------------------
def Souscriptioncreditindex(request):  
    if request.method == "POST":  
        form = SouscriptioncreditForm(request.POST)  
        logger.error("sssssssssssss")
        logger.error(form.errors.as_data())
     
        if form.is_valid():
            try:  
               
                myform=form.save()  
                messages.success(request,"Souscription crédit ajouter avec success")
                return redirect('/assurance/Souscriptioncredit/show')  
            except Exception as e:  
                logger.error( str( e))  
        else:  
            messages.warning(request,"verifier tous les champs")
    else:    
        form = SouscriptioncreditForm()  
    return render(request,'Souscriptioncredit/index3.html',{'form':form})  
def showS(request): 

   
    # Your code
    Souscriptiondecredits = Souscriptiondecredit.objects.all()  
    return render(request,"Souscriptioncredit/show.html",{'Souscriptiondecredits':Souscriptiondecredits})  

 
def destroyS(request, id):  
    instance = Souscriptiondecredit.objects.get(Num_souscription_credit=id)
    instance.delete() 
    messages.warning(request, 'suppression avec succès!')
    return redirect("/assurance/Souscriptioncredit/show")


# -----------------------------Souscription d'assurance voyage-----------------------------------
def Souscriptionvoyageindex(request):
    Beneficiaires = Beneficiaire.objects.all()     
    if request.method == "POST":  
        form = SouscriptionvoyageForm(request.POST)  
        logger.error("sssssssssssss")
        logger.error(form.errors.as_data())
     
        if form.is_valid():
            try:  
               
                myform=form.save()  
                messages.success(request,"Souscription voyage ajouter avec success")
                return redirect('/assurance/Souscriptionvoyage/show')  
            except Exception as e:  
                logger.error( str( e))  
        else:  
            messages.warning(request,"verifier tous les champs")
    else:    
        form = SouscriptionvoyageForm()  
    return render(request,'Souscriptionvoyage/index4.html',{'form':form,'Beneficiaires':Beneficiaires})  
def showSV(request): 

   
    # Your code
    Souscriptiondevoyages = Souscriptiondevoyage.objects.all()  
    return render(request,"Souscriptionvoyage/show.html",{'Souscriptiondevoyages':Souscriptiondevoyages})  
def editSV(request, id):  
    Souscriptiondevoyage1 = Souscriptiondevoyage.objects.get(Num_souscription_voyage=id)  
    return render(request,'Souscriptionvoyage/edit.html', {'Souscriptiondevoyage':Souscriptiondevoyage1})  
def updateSV(request, id):  
    Souscriptiondevoyage1 = Souscriptiondevoyage.objects.get(Num_souscription_voyage=id)  
    form = SouscriptionvoyageForm(request.POST, instance = Souscriptiondevoyage1)  
    
    if form.is_valid():
        try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                
                return redirect('/assurance/Souscriptionvoyage/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'Souscriptionvoyage/edit.html', {'Souscriptiondevoyage': Souscriptiondevoyage1})
 
def destroySV(request, id):  
    instance = Souscriptiondevoyage.objects.get(Num_souscription_voyage=id)
    instance.delete() 
    messages.warning(request, 'suppression avec succès!')
    return redirect("/assurance/Souscriptionvoyage/show")

# -----------------------------beneficiaire-----------------------------------
def beneficiaire(request):  
   
    if request.method == "POST":  
        form = beneficiaireForm(request.POST)  
        logger.error("sssssssssssss")
        logger.error(form.errors.as_data())
        logger.error(form.is_valid())
        if form.is_valid():
            try:  
               
                myform=form.save()  
                messages.success(request,"bénéficiaire ajouter avec success")
                return redirect('/assurance/beneficiaire')  
            except Exception as e:  
                logger.error( str( e))  
        else:  
           messages.warning(request,"verifier tous les champs")
    else:    
        form = beneficiaireForm()  
    return render(request,'beneficiaire/index.html',{'form':form}) 

def showb(request): 

   
    # Your code
    Beneficiaires = Beneficiaire.objects.all()  
    return render(request,"beneficiaire/show.html",{'Beneficiaires':Beneficiaires}) 

# -----------------------------Decision-----------------------------------

def showD(request): 

   
    # Your code
    Souscriptiondecredits = Souscriptiondecredit.objects.all()  
    return render(request,"Decision/show.html",{'Souscriptiondecredits':Souscriptiondecredits})  
def editD(request, id):  
    Souscriptiondecredit1 = Souscriptiondecredit.objects.get(Num_souscription_credit=id)  
    return render(request,'Decision/edit.html', {'Souscriptiondecredit':Souscriptiondecredit1})  
@csrf_exempt    
def updateD1(request):
    if request.is_ajax and request.method == "POST":
        for key in request.POST:  # "for key in request.GET" works too.
    # Add filtering logic here.
            valuelist = request.POST.getlist(key)
            logger.error(valuelist[0])
        Souscriptiondecredit1 = Souscriptiondecredit.objects.get(Num_souscription_credit=valuelist[0])  
        Souscriptiondecredit1.etat_sous_credit="En attente"
        Souscriptiondecredit1.save()
        return JsonResponse({"data": "done"}, status=200) 
    return JsonResponse({"data": "error"}, status=400)        
@csrf_exempt  
def updateD2( request): 
    if request.is_ajax and request.method == "POST":
        for key in request.POST:  # "for key in request.GET" works too.
    # Add filtering logic here.
            valuelist = request.POST.getlist(key)
            logger.error(valuelist[0])
        Souscriptiondecredit1 = Souscriptiondecredit.objects.get(Num_souscription_credit=valuelist[0])  
        Souscriptiondecredit1.etat_sous_credit="Valide"
        Souscriptiondecredit1.save()
        return JsonResponse({"data": "done"}, status=200) 
    return JsonResponse({"data": "error"}, status=400)  
@csrf_exempt  
def updateD3( request): 
    if request.is_ajax and request.method == "POST":
        for key in request.POST:  # "for key in request.GET" works too.
    # Add filtering logic here.
            valuelist = request.POST.getlist(key)
            logger.error(valuelist[0])
        Souscriptiondecredit1 = Souscriptiondecredit.objects.get(Num_souscription_credit=valuelist[0])  
        Souscriptiondecredit1.etat_sous_credit="Refusé"
        Souscriptiondecredit1.save()
        return JsonResponse({"data": "done"}, status=200) 
    return JsonResponse({"data": "error"}, status=400)          
def updateD( request):
    logger.critical('Payment system is not responding')
    logger.error("form.errors.as_data()")  
    Souscriptiondecredit1 = Souscriptiondecredit.objects.get(Num_souscription_credit=id)  
    form = SouscriptioncreditForm(request.POST, instance = Souscriptiondecredit1)  
    logger.error(form.errors.as_data())
    if form.is_valid():
        try:  
                logger.error("save begin")
                logger.error(form)
                myform=form.save()  
                
                return redirect('/assurance/Decision/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'Decision/edit.html', {'Souscriptiondecredit': Souscriptiondecredit1})
 