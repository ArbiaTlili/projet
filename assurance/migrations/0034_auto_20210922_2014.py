# Generated by Django 3.1.7 on 2021-09-22 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0033_auto_20210918_0102'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produitassurance',
            new_name='Produitvoyage',
        ),
        migrations.RemoveField(
            model_name='baremedecredit',
            name='code_produit',
        ),
        migrations.RemoveField(
            model_name='souscriptiondecredit',
            name='code_produit',
        ),
        migrations.CreateModel(
            name='Produitcredit',
            fields=[
                ('code_produitC', models.AutoField(primary_key=True, serialize=False)),
                ('libelle_produit', models.CharField(max_length=20)),
                ('Num_parteneriat', models.IntegerField(blank=True)),
                ('part_banque', models.CharField(blank=True, max_length=30)),
                ('part_assureur', models.CharField(blank=True, max_length=30)),
                ('retenue_source', models.CharField(blank=True, max_length=30)),
                ('TVA', models.IntegerField(blank=True)),
                ('Frais_MEP_asssureur', models.CharField(blank=True, max_length=30)),
                ('Frais_MEP_banque', models.CharField(blank=True, max_length=30)),
                ('Niveau_validation', models.CharField(max_length=30)),
                ('age_seuil', models.IntegerField()),
                ('montant_seuil', models.IntegerField()),
                ('etat_produit', models.CharField(choices=[('Valide', 'Valide'), ('En attente', 'En attente')], max_length=40)),
                ('code_assureur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assurance.assureur')),
            ],
        ),
        migrations.AddField(
            model_name='baremedecredit',
            name='code_produitC',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assurance.produitcredit', unique=True),
        ),
        migrations.AddField(
            model_name='souscriptiondecredit',
            name='code_produitC',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='assurance.produitcredit'),
        ),
    ]
