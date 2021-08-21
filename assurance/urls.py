from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    path('agentsécurité',views.base2, name="agentsécurité"),
    path('utilisateurs',views.utilisateurs, name="utilisateurs"),
    path('groupe',views.groupe, name="groupe"),
    path('droits',views.droits, name="droits"),
    path('privilège',views.privilège, name="privilège"),
    path('compte',views.compte, name="compte"),

    path('clientèle',views.base3, name="clientèle"),
    path('sousvoyage',views.sousvoyage, name="sousvoyage"),
    path('souscrédit',views.souscrédit, name="souscrédit"),
    path('compte1',views.compte1, name="compte1"),

    path('backoffice',views.base1, name="backoffice"),
    path('compagnies',views.compagnies, name="compagnies"),
    path('produit',views.produit, name="produit"),
    path('barémescrédit',views.barémescrédit, name="barémescrédit"),
    path('barémesvoyage',views.barémesvoyage, name="barémesvoyage"),
    path('décision',views.décision, name="décision"),
    path('compte2',views.compte2, name="compte2"),

    path('ajt_user/',views.ajt_user, name="ajt_user"),

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

]
