# Generated by Django 3.2.6 on 2021-09-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0017_auto_20210910_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
