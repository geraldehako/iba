# Generated by Django 4.1.7 on 2023-06-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administrations", "0022_matrimoniales_etudiants_matrimoniale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ecoles",
            name="Etablissement",
            field=models.CharField(max_length=250),
        ),
    ]
