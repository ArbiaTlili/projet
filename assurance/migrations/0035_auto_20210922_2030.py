# Generated by Django 3.1.7 on 2021-09-22 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0034_auto_20210922_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baremedecredit',
            name='code_produitC',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assurance.produitcredit'),
        ),
    ]