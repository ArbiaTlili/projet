# Generated by Django 3.1.7 on 2021-09-15 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0023_auto_20210915_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produitassurance',
            old_name='code_produit',
            new_name='code_du_produit',
        ),
        migrations.RemoveField(
            model_name='souscriptiondevoyage',
            name='code_produit',
        ),
        migrations.AddField(
            model_name='souscriptiondevoyage',
            name='Code_produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assurance.produitassurance'),
        ),
    ]
