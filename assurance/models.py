from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
# Create your models here.
class Admin(models.Model):
    user = models.OneToOneField(User,null=False,blank=False,on_delete = models.CASCADE)
  # extra files will come here
    phone_field = models.CharField(max_length=12,blank=False)

class Groupe(models.Model):
  code_groupe = models.AutoField(primary_key = True)
  Libelle_groupe = models.IntegerField(null=False)

    
  
      


class Unitedegestion(models.Model):
  UG_actuel_id = models.AutoField(primary_key = True)
  type_UG = models.CharField(max_length=40)
  Libelle_UG = models.IntegerField(null=False)
  code_UG_BCT = models.CharField(max_length=40)
  

      
    
  

class Utilisateur(models.Model):
  Code_utilisateur= models.AutoField(primary_key = True)
  NomPrenom_utilisateur= models.CharField(max_length=40)
  MotDePasse=models.CharField(max_length=50)
  Email_utilisateur = models.EmailField(max_length=254)
  code_groupe=  models.ForeignKey(
        'Groupe',
        on_delete=models.CASCADE,
    )
  UG_actuel_id =  models.ForeignKey(
        'Unitedegestion',
        on_delete=models.CASCADE,null=False
    )
    

    

  
class ClientUIB(models.Model):
  Num_fiche_client = models.AutoField(primary_key = True)
  Num_cin_UIB = models.IntegerField(null=False)
  Nom = models.CharField(max_length=40)
  Prenom = models.CharField(max_length=40)
  Date_Naissance = models.DateTimeField(auto_now=True)
  Lieu_Naissance = models.CharField(max_length=40)
  Adresse = models.CharField(max_length=40)
  Profession = models.CharField(max_length=40)
  Telephone = PhoneNumberField(null=False, blank=False, unique=True)
  Categorie_client = models.CharField(max_length=20)
  Declaration_maladie = models.CharField(max_length=40)

def __str__(self):
    return self.Num_fiche_client



class Comptebancaire(models.Model):
  code_NCP = models.AutoField(primary_key = True)
  code_UG_BCT=models.IntegerField(null=False)
  num_fiche_client=models.ForeignKey(
  'ClientUIB',
  on_delete=models.CASCADE,
  )
  Solde = models.IntegerField(null=False)

    
 
 


class Credit(models.Model):
    Num_dossierCredit = models.AutoField(primary_key = True)
    Num_compte = models.IntegerField(null=False)
    Montant_credit = models.IntegerField(null=False)
    Date_premiereEcheance = models.DateTimeField(auto_now=True)
    Date_derniereEcheance = models.DateTimeField(auto_now=True)
    Date_deblocage = models.DateTimeField(auto_now=True)
    Durée_crédit = models.CharField(max_length=40)
    
def __str__(self):
    return self.Num_dossierCredit
   



class Assureur(models.Model):
    code_assureur = models.AutoField(primary_key = True)
    Nom_assureur = models.CharField(max_length=40)
    code_NCP=models.ForeignKey(
    'Comptebancaire',
    on_delete=models.CASCADE,null=True
    )
    code_NCP = models.OneToOneField("Comptebancaire", on_delete=models.CASCADE, null= True)
    Adresse = models.CharField(max_length=40)
    contact = models.CharField(max_length=40)
    Telephone = PhoneNumberField(null=False, blank=False)
    fax = models.CharField(max_length=20)
    Email = models.EmailField(max_length=254)
    Agence = models.CharField(max_length=20)
    
def __str__(self):
    return self.code_assureur

    
    
class Produitcredit(models.Model):
    code_produitC = models.AutoField(primary_key = True)
    libelle_produit = models.CharField(max_length=20, null=False)
    code_assureur =models.OneToOneField('Assureur' ,on_delete=models.CASCADE)
    Num_parteneriat = models.IntegerField(blank=True)
    part_banque =models.CharField(max_length=30, blank=False)
    part_assureur =models.CharField(max_length=30,blank=False )
    retenue_source=models.CharField(max_length=30, blank=False)
    TVA =models.IntegerField(blank=True)
    Frais_MEP_asssureur=models.CharField(max_length=30, blank=False)
    Frais_MEP_banque =models.CharField(max_length=30, blank=False)
    Niveau_validation =models.CharField(max_length=30)
    age_seuil =models.IntegerField(null=False)
    montant_seuil =models.IntegerField(null=False)
    Valide='Valide'
    En_attente='En attente'
    COUVERTURE_CHOICES = [   
      ('Valide', 'Valide'),
      ('En attente', 'En attente'),
      ]
    etat_produit= models.CharField(choices=COUVERTURE_CHOICES, max_length=40) 


class Produitvoyage(models.Model):
    code_produit = models.AutoField(primary_key = True)
    libelle_produit = models.CharField(max_length=20, null=False)
    code_assureur = models.OneToOneField('Assureur', on_delete=models.CASCADE)
    Num_parteneriat = models.IntegerField(blank=True)
    part_banque =models.CharField(max_length=30, blank=False)
    part_assureur =models.CharField(max_length=30,blank=False )
    retenue_source=models.CharField(max_length=30, blank=False)
    TVA =models.IntegerField(blank=True)
    Frais_MEP_asssureur=models.CharField(max_length=30, blank=False)
    Frais_MEP_banque =models.CharField(max_length=30, blank=False)
    Niveau_validation =models.CharField(max_length=30)
    age_seuil =models.IntegerField(null=False)
    montant_seuil =models.IntegerField(null=False)
    Valide='Valide'
    En_attente='En attente'
    COUVERTURE_CHOICES = [   
      ('Valide', 'Valide'),
      ('En attente', 'En attente'),
      ]
    etat_produit= models.CharField(choices=COUVERTURE_CHOICES, max_length=40) 
    
    




class Baremedecredit(models.Model):
    id_bareme_credit = models.AutoField(primary_key = True) 
    code_assureur =models.OneToOneField('Assureur' ,on_delete=models.CASCADE, null= True)
    code_produitC = models.OneToOneField("Produitcredit", on_delete=models.CASCADE, null= True)
    age_min =models.IntegerField(null=False)
    age_max =models.IntegerField(null=False)
    date_debut = models.DateTimeField(default=datetime.now(), blank=True)
    duree = models.CharField(max_length=40, null=True) 
    taux_assureur = models.IntegerField(null=False)
    marge_banque = models.IntegerField(null=False)
    etat_bareme= models.CharField(max_length=30)
    

 
    
        
class Baremedevoyage(models.Model):
    id_bareme_voyage = models.AutoField(primary_key =True)
    code_produit = models.OneToOneField("Produitvoyage", on_delete=models.CASCADE, null=True)
    duree = models.IntegerField(null=False)
    taux_assureur = models.IntegerField(null=False)
    marge_banque = models.IntegerField(null=False)
    Valide='Valide'
    En_attente='En attente'
    COUVERTURE_CHOICES = [   
      ('Valide', 'Valide'),
      ('En attente', 'En attente'),
      ]
    etat_bareme= models.CharField(choices=COUVERTURE_CHOICES, max_length=40)      
    I='Individuel'
    F='Familiale'
    COUVERTURE_CHOICES = [   
      ('I', 'Individuel'),
      ('F', 'Familiale'),
      ]
    type_couverture = models.CharField(choices=COUVERTURE_CHOICES, max_length=40)
   


class Souscriptiondecredit(models.Model):
    Num_souscription_credit = models.AutoField(primary_key = True)
    Num_dossierCredit = models.OneToOneField("Credit", on_delete=models.CASCADE, null=True)
    code_produitC = models.OneToOneField("Produitcredit", on_delete=models.CASCADE, null=True)
    montant_assurance = models.IntegerField(null=False)
    Valide='Valide'
    En_attente='En attente'
    COUVERTURE_CHOICES = [   
      ('Valide', 'Valide'),
      ('En attente', 'En attente'),
      ]
    etat_sous_credit =models.CharField(choices=COUVERTURE_CHOICES, max_length=40)
    
    
   


class Souscriptiondevoyage(models.Model):
    Num_souscription_voyage = models.AutoField(primary_key = True)
    Num_fiche_client = models.OneToOneField("ClientUIB", on_delete=models.CASCADE, null=True)
    code_assureur = models.OneToOneField('Produitvoyage', on_delete=models.CASCADE,)
    I='Individuel'
    F='Familiale'
    COUVERTURE_CHOICES = [   
      ('I', 'Individuel'),
      ('F', 'Familiale'),
      ]
    type_couverture = models.CharField(choices=COUVERTURE_CHOICES, max_length=40)
    duree = models.CharField(max_length=40)
    date_debut = models.DateTimeField(default=datetime.now(), blank=True) 
    montant_assurance = models.IntegerField(null=False)
    beneficiaires= models.CharField(null=True,  blank=True, max_length=40)
    

    
    

class Beneficiaire(models.Model):
    id_beneficiaire = models.AutoField(primary_key = True) 
    Num_souscription_voyage = models.ForeignKey(
    'Souscriptiondevoyage',
    on_delete=models.CASCADE,null=True
    )
    nom_beneficiaire = models.CharField(max_length=40)
    prenom_beneficiaire = models.CharField(max_length=40)
    date_naissance = models.DateTimeField(auto_now=True)
    relation =  models.CharField(max_length=40)  
    num_document = models.IntegerField(null=False)
    