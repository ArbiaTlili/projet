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
]

