# Generated by Django 3.2.6 on 2021-08-17 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produitassurance',
            name='code_assureur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assurance.assureur'),
        ),
    ]
