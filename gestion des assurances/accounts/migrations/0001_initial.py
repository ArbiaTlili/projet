# Generated by Django 3.2.6 on 2021-08-08 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assureur',
            fields=[
                ('code_assureur', models.AutoField(primary_key=True, serialize=False)),
                ('Nom_assureur', models.CharField(max_length=40)),
                ('Adresse', models.CharField(max_length=40)),
                ('contact', models.CharField(max_length=40)),
                ('Telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('fax', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Agence', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Baremedevoyage',
            fields=[
                ('id_bareme_voyage', models.AutoField(primary_key=True, serialize=False)),
                ('duree', models.IntegerField()),
                ('taux_assureur', models.IntegerField()),
                ('marge_banque', models.IntegerField()),
                ('etat_bareme', models.CharField(max_length=30)),
                ('type_couverture', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiaire',
            fields=[
                ('id_beneficiaire', models.AutoField(primary_key=True, serialize=False)),
                ('num_souscription', models.IntegerField()),
                ('nom_beneficiaire', models.CharField(max_length=40)),
                ('prenom_beneficiaire', models.CharField(max_length=40)),
                ('date_naissance', models.DateTimeField(auto_now=True)),
                ('type_document', models.CharField(max_length=40)),
                ('relation', models.CharField(max_length=40)),
                ('num_document', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientpassager',
            fields=[
                ('Num_cin_passager', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=40)),
                ('Prenom', models.CharField(max_length=40)),
                ('Date_Naissance', models.DateTimeField(auto_now=True)),
                ('Lieu_Naissance', models.CharField(max_length=40)),
                ('Adresse', models.CharField(max_length=40)),
                ('Profession', models.CharField(max_length=40)),
                ('Telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Categorie_client', models.CharField(max_length=20)),
                ('Declaration_maladie', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ClientUIB',
            fields=[
                ('Num_fiche_client', models.AutoField(primary_key=True, serialize=False)),
                ('Num_cin_UIB', models.IntegerField()),
                ('Nom', models.CharField(max_length=40)),
                ('Prenom', models.CharField(max_length=40)),
                ('Date_Naissance', models.DateTimeField(auto_now=True)),
                ('Lieu_Naissance', models.CharField(max_length=40)),
                ('Adresse', models.CharField(max_length=40)),
                ('Profession', models.CharField(max_length=40)),
                ('Telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Categorie_client', models.CharField(max_length=20)),
                ('Declaration_maladie', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('Num_dossierCredit', models.AutoField(primary_key=True, serialize=False)),
                ('Num_compte', models.IntegerField()),
                ('Montant_credit', models.IntegerField()),
                ('Date_premiereEcheance', models.DateTimeField(auto_now=True)),
                ('Date_derniereEcheance', models.DateTimeField(auto_now=True)),
                ('Date_deblocage', models.DateTimeField(auto_now=True)),
                ('Durée_crédit', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('code_groupe', models.AutoField(primary_key=True, serialize=False)),
                ('Libelle_groupe', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produitassurance',
            fields=[
                ('code_produit', models.AutoField(primary_key=True, serialize=False)),
                ('libelle_produit', models.CharField(max_length=20)),
                ('Num_parteneriat', models.IntegerField()),
                ('type_produit', models.CharField(max_length=30)),
                ('code_assureur', models.IntegerField()),
                ('part_banque', models.CharField(max_length=30)),
                ('part_assureur', models.CharField(max_length=30)),
                ('retenue_source', models.CharField(max_length=30)),
                ('TVA', models.IntegerField()),
                ('Frais_MEP_asssureur', models.CharField(max_length=30)),
                ('Frais_MEP_banque', models.CharField(max_length=30)),
                ('Niveau_validation', models.CharField(max_length=30)),
                ('Periodicite_renversement', models.CharField(max_length=30)),
                ('age_seuil', models.IntegerField()),
                ('montant_seuil', models.IntegerField()),
                ('etat_produit', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Unitedegestion',
            fields=[
                ('UG_actuel_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_UG', models.CharField(max_length=40)),
                ('Libelle_UG', models.IntegerField()),
                ('code_UG_BCT', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('Code_utilisateur', models.AutoField(primary_key=True, serialize=False)),
                ('NomPrenom_utilisateur', models.CharField(max_length=40)),
                ('MotDePasse', models.CharField(max_length=50)),
                ('Email_utilisateur', models.EmailField(max_length=254)),
                ('UG_actuel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.unitedegestion')),
                ('code_groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.groupe')),
            ],
        ),
        migrations.CreateModel(
            name='Souscriptiondevoyage',
            fields=[
                ('Num_souscription_voyage', models.AutoField(primary_key=True, serialize=False)),
                ('id_client', models.IntegerField()),
                ('montant_assurance', models.IntegerField()),
                ('duree', models.IntegerField()),
                ('code_produit', models.IntegerField()),
                ('date_debut', models.DateTimeField(auto_now=True)),
                ('type_client', models.CharField(max_length=40)),
                ('etat_sous_credit', models.CharField(max_length=40)),
                ('type_couverture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.baremedevoyage')),
            ],
        ),
        migrations.CreateModel(
            name='Souscriptiondecredit',
            fields=[
                ('Num_souscription_credit', models.AutoField(primary_key=True, serialize=False)),
                ('montant_assurance', models.IntegerField()),
                ('etat_sous_credit', models.CharField(max_length=20)),
                ('Num_dossierCredit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.credit')),
                ('code_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.produitassurance')),
            ],
        ),
        migrations.CreateModel(
            name='Comptebancaire',
            fields=[
                ('code_NCP', models.AutoField(primary_key=True, serialize=False)),
                ('code_UG_BCT', models.IntegerField()),
                ('Solde', models.IntegerField()),
                ('num_fiche_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.clientuib')),
            ],
        ),
        migrations.AddField(
            model_name='baremedevoyage',
            name='code_produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produitassurance', to='accounts.produitassurance'),
        ),
        migrations.AddField(
            model_name='baremedevoyage',
            name='produitassurance',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.produitassurance'),
        ),
        migrations.CreateModel(
            name='Baremedecredit',
            fields=[
                ('id_bareme_credit', models.AutoField(primary_key=True, serialize=False)),
                ('age_min', models.IntegerField()),
                ('age_max', models.IntegerField()),
                ('duree_min', models.DateTimeField(auto_now=True)),
                ('duree_max', models.DateTimeField(auto_now=True)),
                ('taux_assureur', models.IntegerField()),
                ('marge_banque', models.IntegerField()),
                ('etat_bareme', models.CharField(max_length=30)),
                ('code_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produitassurancee', to='accounts.produitassurance')),
                ('produitassurancee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.produitassurance')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_field', models.CharField(max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
