from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
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

   

class Clientpassager(models.Model):
  Num_cin_passager = models.AutoField(primary_key = True)
  Nom = models.CharField(max_length=40)
  Prenom = models.CharField(max_length=40)
  Date_Naissance = models.DateTimeField(auto_now=True)
  Lieu_Naissance = models.CharField(max_length=40)
  Adresse = models.CharField(max_length=40)
  Profession = models.CharField(max_length=40)
  Telephone = PhoneNumberField(null=False, blank=False, unique=True)
  Categorie_client =models.CharField(max_length=20)
  Declaration_maladie = models.CharField(max_length=40)
    

   
  

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
    

   



class Assureur(models.Model):
    code_assureur = models.AutoField(primary_key = True)
    Nom_assureur = models.CharField(max_length=40)
    Adresse = models.CharField(max_length=40)
    contact = models.CharField(max_length=40)
    Telephone = PhoneNumberField(null=False, blank=False, unique=True)
    fax = models.CharField(max_length=20)
    Email = models.EmailField(max_length=254)
    Agence = models.CharField(max_length=20)
    

    
    

class Produitassurance(models.Model):
    code_produit = models.AutoField(primary_key = True)
    libelle_produit = models.CharField(max_length=20)
    Num_parteneriat = models.IntegerField(null=False)
    type_produit = models.CharField(max_length=30)
    code_assureur =models.ForeignKey('Assureur' ,on_delete=models.CASCADE)
    part_banque =models.CharField(max_length=30)
    part_assureur =models.CharField(max_length=30)
    retenue_source=models.CharField(max_length=30)
    TVA =models.IntegerField()
    Frais_MEP_asssureur=models.CharField(max_length=30)
    Frais_MEP_banque =models.CharField(max_length=30)
    Niveau_validation =models.CharField(max_length=30)
    Periodicite_renversement =models.CharField(max_length=30)
    age_seuil =models.IntegerField(null=False)
    montant_seuil =models.IntegerField(null=False)
    etat_produit =models.CharField(max_length=30)
    

   

class Baremedecredit(models.Model):
    id_bareme_credit = models.AutoField(primary_key = True) 
    code_produit = models.ForeignKey(
    'Produitassurance',
    on_delete=models.CASCADE, related_name ='produitassurancee'
    )
    age_min =models.IntegerField(null=False)
    age_max =models.IntegerField(null=False)
    date_debut = models.DateTimeField(auto_now=True)
    duree = models.CharField(max_length=40, null=True) 
    taux_assureur = models.IntegerField(null=False)
    marge_banque = models.IntegerField(null=False)
    etat_bareme= models.CharField(max_length=30)
    produitassurancee = models.OneToOneField("Produitassurance", on_delete=models.CASCADE, null= True)

 
    
        
class Baremedevoyage(models.Model):
    id_bareme_voyage = models.AutoField(primary_key =True)
    code_produit = models.ForeignKey(
    'Produitassurance',
    on_delete=models.CASCADE,related_name = 'Produitassurance'
    )  
    duree = models.IntegerField(null=False)
    taux_assureur = models.IntegerField(null=False)
    marge_banque = models.IntegerField(null=False)
    etat_bareme= models.CharField(max_length=30)      
    I='Individuel'
    F='Familiale'
    COUVERTURE_CHOICES = [   
      ('I', 'Individuel'),
      ('F', 'Familiale'),
      ]
    type_couverture = models.CharField(choices=COUVERTURE_CHOICES, max_length=40)
   


class Souscriptiondecredit(models.Model):
    Num_souscription_credit = models.AutoField(primary_key = True)
    Num_dossierCredit = models.ForeignKey(
    'Credit',
    on_delete=models.CASCADE,
    )
    code_produit = models.ForeignKey(
    'Produitassurance',
    on_delete=models.CASCADE,
    )
    montant_assurance = models.IntegerField(null=False)
    etat_sous_credit = models.CharField(max_length=20)
    

   


class Souscriptiondevoyage(models.Model):
    Num_souscription_voyage = models.AutoField(primary_key = True)
    UIB='client UIB'
    P='client passager'
    CLIENT_CHOICES = [   
      ('UIB', 'client UIB'),
      ('P', 'client passager'),
      ]
    type_client = models.CharField(choices=CLIENT_CHOICES, max_length=40)
    Num_cin_passager = models.ForeignKey(
    'Clientpassager',
    on_delete=models.CASCADE, null=False
    )
    Num_fiche_client = models.ForeignKey(
    'ClientUIB',
    on_delete=models.CASCADE, null=False
    )
    Num_compte = models.IntegerField(null=True)
    code_assureur =models.IntegerField(null=False)
    code_produit = models.ForeignKey(
    'Produitassurance',
    on_delete=models.CASCADE, null=True
    )
    I='Individuel'
    F='Familiale'
    COUVERTURE_CHOICES = [   
      ('I', 'Individuel'),
      ('F', 'Familiale'),
      ]
    type_couverture = models.CharField(choices=COUVERTURE_CHOICES, max_length=40)
    duree = models.IntegerField(null=False)
    date_debut =models.DateTimeField(auto_now=True) 
    montant_assurance = models.IntegerField(null=False)
   
    

    
    

class Beneficiaire(models.Model):
    id_beneficiaire = models.AutoField(primary_key = True) 
    num_souscription = models.IntegerField(null=False)
    nom_beneficiaire = models.CharField(max_length=40)
    prenom_beneficiaire = models.CharField(max_length=40)
    date_naissance = models.DateTimeField(auto_now=True)
    type_document = models.CharField(max_length=40)
    relation =  models.CharField(max_length=40)  
    num_document = models.IntegerField(null=False)
    