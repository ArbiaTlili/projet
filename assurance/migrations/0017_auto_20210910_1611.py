# Generated by Django 3.1.7 on 2021-09-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0016_souscriptiondevoyage_beneficiaires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souscriptiondevoyage',
            name='beneficiaires',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
