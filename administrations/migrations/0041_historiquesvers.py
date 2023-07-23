# Generated by Django 4.1.7 on 2023-07-07 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("administrations", "0040_alter_dossierfinances_montantrestant_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoriquesVers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Datevers", models.DateField(null=True)),
                (
                    "Montantscolarité",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "Montantversé",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "Montantrestant",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "Montantvers",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("Nom", models.CharField(max_length=100, null=True)),
                ("Ecole", models.CharField(max_length=100, null=True)),
                ("Sexe", models.CharField(max_length=10, null=True)),
                (
                    "Anneescolaire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.anneescolaires",
                    ),
                ),
                (
                    "Dossierfinance",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.dossierfinances",
                    ),
                ),
                (
                    "Etudiant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.etudiants",
                    ),
                ),
                (
                    "Niveau",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.niveaux",
                    ),
                ),
                (
                    "Salle",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.salles",
                    ),
                ),
            ],
        ),
    ]
