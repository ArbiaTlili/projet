# Generated by Django 3.1.7 on 2021-08-30 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0008_auto_20210830_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='souscriptiondevoyage',
            name='Num_compte',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='souscriptiondevoyage',
            name='type_couverture',
            field=models.CharField(choices=[('I', 'Individuel'), ('F', 'Familiale')], max_length=40),
        ),
    ]
