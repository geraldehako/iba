# Generated by Django 4.1.7 on 2023-07-07 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("administrations", "0036_remove_autorisationsauditeur_poste_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dossierscolaires",
            name="Contact",
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Datenaissance",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Ecole",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.ecoles",
            ),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Email",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Lieunaissance",
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Matricule",
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Matrimoniale",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.matrimoniales",
            ),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Niveau",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.niveaux",
            ),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Nom",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Photo",
            field=models.ImageField(null=True, upload_to="Images/Photos/etudiants"),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Prenoms",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Salle",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.salles",
            ),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Sexe",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.genres",
            ),
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="Telephone",
            field=models.CharField(max_length=15, null=True),
        ),
    ]
