# Generated by Django 4.1.7 on 2023-03-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrations", "0015_etudiants_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="etudiants",
            name="Matricule",
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
