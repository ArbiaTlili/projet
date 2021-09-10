from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    path('agentsécurité',views.base2, name="agentsécurité"),
    

    path('clientèle',views.base3, name="clientèle"),
    path('backoffice',views.base1, name="backoffice"),
    path('décision',views.décision, name="décision"),
    #client
    path('client',views.base4, name="client"),
    #about
    path('about',views.base5, name="about"),
    #home
    path('home',views.home, name="home"),
    # produit assurance

    path('produitAssurance', views.produitAssurance ,name='produitAssurance'),  
    
    path('produitAssurance/show',views.showPA), 
    path('produitAssurance/edit/<int:id>', views.editPA),  
    path('produitAssurance/update/<int:id>', views.updatePA),  
    path('produitAssurance/delete/<int:id>', views.destroyPA),  
    
    # Assureur

    path('Assureur', views.Assureurindex ,name='Assureurindex'),  
    
    path('Assureur/show',views.showA), 
    path('Assureur/edit/<int:id>', views.editA),  
    path('Assureur/update/<int:id>', views.updateA),  
    path('Assureur/delete/<int:id>', views.destroyA),  


    #Baremedevoyage

    path('Baremevoyage', views.Baremevoyageindex ,name='Baremevoyageindex'),  
    path('Baremevoyage/show',views.showB), 
    path('Baremevoyage/edit/<int:id>', views.editB),  
    path('Baremevoyage/update/<int:id>', views.updateB),  
    path('Baremevoyage/delete/<int:id>', views.destroyB),  


     #Baremedecredit

    path('Baremecredit', views.Baremecreditindex ,name='Baremecreditindex'),  
    path('Baremecredit/show',views.showC), 
    path('Baremecredit/edit/<int:id>', views.editC),  
    path('Baremecredit/update/<int:id>', views.updateC),  
    path('Baremecredit/delete/<int:id>', views.destroyC),  


  #Souscriptiondecredit

    path('Souscriptioncredit', views.Souscriptioncreditindex ,name='Souscriptioncreditindex'),  
    path('Souscriptioncredit/show',views.showS), 
    path('Souscriptioncredit/delete/<int:id>', views.destroyS),

#Souscriptiondevoyage

    path('Souscriptionvoyage', views.Souscriptionvoyageindex ,name='Souscriptionvoyageindex'),  
    path('Souscriptionvoyage/show',views.showSV), 
    path('Souscriptionvoyage/edit/<int:id>', views.editSV),  
    path('Souscriptionvoyage/update/<int:id>', views.updateSV),  
    path('Souscriptionvoyage/delete/<int:id>', views.destroySV),
#Beneficiaire
    path('beneficiaire', views.beneficiaire ,name='beneficiaire'),
    path('beneficiaire/show',views.showb), 


#Decision
    path('decision/show',views.showD, name= 'Decision'), 
    path('decision/edit/<int:id>', views.editD),  
    path('decision/update/<int:id>', views.updateD),
    path('decision/update1', views.updateD1), 
    path('decision/update2', views.updateD2),
]
