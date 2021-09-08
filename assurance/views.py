
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render, redirect  
from django.contrib import messages
from assurance.forms import ProduitassuranceForm ,AssureurForm, BaremeassurancevoyageForm, BaremeassurancecreditForm, SouscriptioncreditForm, SouscriptionvoyageForm, beneficiaireForm  
from assurance.models import Produitassurance ,Assureur, Baremedevoyage, Baremedecredit, Souscriptiondecredit,  Souscriptiondevoyage, Beneficiaire
from django.contrib.auth.models import Permission
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

     
def base4(request):
      
    return render(request, 'base4.html')

def base5(request):
      
    return render(request, 'base5.html')    

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
        messages.error(request,"verifier tous les champs")
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
                messages.success(request, 'Update successful!')
                return redirect('/assurance/Baremevoyage/show')  
            except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'Baremevoyage/edit.html', {'Baremedevoyage': Baremedevoyage1})  
def destroyB(request, id):  
    instance = Baremedevoyage.objects.get(id_bareme_voyage=id)
    instance.delete()
    messages.success(request, 'Deleted successful!')
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
        messages.error(request,"verifier tous les champs")
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
                
                return redirect('/assurance/Baremecredit/show')  
        except Exception as e:  
                logger.error( str( e))   

         
    return render(request, 'Baremecredit/edit.html', {'Baremedecredit': Baremedecredit1})  
def destroyC(request, id):  
    instance = Baremedecredit.objects.get(id_bareme_credit=id)
    instance.delete() 
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
        messages.error(request,"verifier tous les champs")
        form = SouscriptioncreditForm()  
    return render(request,'Souscriptioncredit/index3.html',{'form':form,'Beneficiaires':Beneficiaires})  
def showS(request): 

   
    # Your code
    Souscriptiondecredits = Souscriptiondecredit.objects.all()  
    return render(request,"Souscriptioncredit/show.html",{'Souscriptiondecredits':Souscriptiondecredits})  

 
def destroyS(request, id):  
    instance = Souscriptiondecredit.objects.get(Num_souscription_credit=id)
    instance.delete() 
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
        messages.error(request,"verifier tous les champs")
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
        messages.error(request,"verifier tous les champs")
        form = beneficiaireForm()  
    return render(request,'beneficiaire/index.html',{'form':form}) 