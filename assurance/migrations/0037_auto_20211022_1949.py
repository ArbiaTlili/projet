# Generated by Django 3.1.7 on 2021-10-22 17:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0036_remove_produitvoyage_type_produit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baremedecredit',
            name='code_assureur',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='assurance.assureur'),
        ),
        migrations.AlterField(
            model_name='baremedecredit',
            name='code_produitC',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='assurance.produitcredit'),
        ),
        migrations.AlterField(
            model_name='baremedecredit',
            name='date_debut',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 22, 19, 49, 55, 357104)),
        ),
        migrations.AlterField(
            model_name='produitcredit',
            name='code_assureur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assurance.assureur'),
        ),
        migrations.AlterField(
            model_name='produitvoyage',
            name='code_assureur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assurance.assureur'),
        ),
    ]
