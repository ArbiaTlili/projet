# Generated by Django 3.1.7 on 2021-08-21 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0006_auto_20210821_0436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baremedevoyage',
            name='produitassurance',
        ),
    ]