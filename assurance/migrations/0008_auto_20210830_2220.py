# Generated by Django 3.1.7 on 2021-08-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0007_remove_baremedevoyage_produitassurance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='souscriptiondevoyage',
            old_name='code_produit',
            new_name='code_assureur',
        ),
        migrations.RemoveField(
            model_name='souscriptiondevoyage',
            name='etat_sous_credit',
        ),
        migrations.AlterField(
            model_name='souscriptiondevoyage',
            name='type_client',
            field=models.CharField(choices=[('UIB', 'client UIB'), ('P', 'client passager')], max_length=40),
        ),
    ]
