# Generated by Django 3.1.7 on 2021-09-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0022_auto_20210915_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produitassurance',
            name='Num_parteneriat',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='produitassurance',
            name='type_produit',
            field=models.CharField(choices=[('Assurance_Crédit', 'Assurance crédit'), ('Assurance_Voyage', 'Assurance voyage')], max_length=50),
        ),
    ]
