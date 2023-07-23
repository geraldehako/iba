# Generated by Django 4.1.7 on 2023-07-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="utilisateur",
            name="statut",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="utilisateur",
            name="role",
            field=models.CharField(
                choices=[
                    ("GESTIONNAIRE", "Gestionnaire"),
                    ("ENSEIGNANT", "Enseignant"),
                    ("ETUDIANT", "Etudiant"),
                    ("ADMINISTRATEUR", "Administrateur"),
                ],
                max_length=30,
                verbose_name="rôle",
            ),
        ),
    ]