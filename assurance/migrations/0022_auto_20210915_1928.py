# Generated by Django 3.1.7 on 2021-09-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0021_auto_20210914_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produitassurance',
            name='id_code',
        ),
        migrations.AlterField(
            model_name='produitassurance',
            name='code_produit',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produitassurance',
            name='type_produit',
            field=models.CharField(choices=[('Assurance_Crédit', 'Assurance crédit'), ('Assurance_Voyage', 'Assurance voyage')], max_length=40),
        ),
    ]
