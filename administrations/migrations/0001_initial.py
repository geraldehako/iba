# Generated by Django 4.1.7 on 2023-03-18 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ecoles",
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
                ("Etablissement", models.CharField(max_length=50)),
                ("Ville", models.CharField(max_length=50, null=True)),
                ("Telephone", models.CharField(max_length=15, null=True)),
                ("Contact", models.CharField(max_length=15, null=True)),
                ("Adresse", models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Genres",
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
                ("Sexe", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Niveaux",
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
                ("Niveauetude", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Statuts",
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
                ("Statut", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Typeecoles",
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
                ("Typeecole", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Typematieres",
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
                ("Typematiere", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Salles",
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
                ("Salle", models.CharField(max_length=50)),
                ("Nbreplace", models.IntegerField()),
                (
                    "Niveau",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.niveaux",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Matieres",
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
                ("Matiere", models.CharField(max_length=50)),
                (
                    "Typematiere",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.typematieres",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Etudiants",
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
                ("Nom", models.CharField(max_length=100)),
                ("Prenoms", models.CharField(max_length=250)),
                ("Datenaissance", models.DateField(null=True)),
                ("Lieunaissance", models.CharField(max_length=15, null=True)),
                ("Telephone", models.CharField(max_length=15, null=True)),
                ("Contact", models.CharField(max_length=15, null=True)),
                ("Email", models.CharField(max_length=50, null=True)),
                ("Photo", models.ImageField(null=True, upload_to="Etudiants")),
                (
                    "Ecole",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.ecoles",
                    ),
                ),
                (
                    "Niveau",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.niveaux",
                    ),
                ),
                (
                    "Salle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.salles",
                    ),
                ),
                (
                    "Sexe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.genres",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Enseignants",
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
                ("Matricule", models.CharField(max_length=100, null=True)),
                ("Nom", models.CharField(max_length=100)),
                ("Prenoms", models.CharField(max_length=250)),
                ("Datenaissance", models.DateField(null=True)),
                ("Lieunaissance", models.CharField(max_length=15, null=True)),
                ("Telephone", models.CharField(max_length=15, null=True)),
                ("Contact", models.CharField(max_length=15, null=True)),
                ("Email", models.CharField(max_length=50, null=True)),
                (
                    "Photo",
                    models.ImageField(blank=True, null=True, upload_to="Etudiants/"),
                ),
                (
                    "Ecole",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.ecoles",
                    ),
                ),
                (
                    "Matiere",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.matieres",
                    ),
                ),
                (
                    "Sexe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.genres",
                    ),
                ),
                (
                    "Statut",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.statuts",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="ecoles",
            name="Natureecole",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.typeecoles",
            ),
        ),
        migrations.CreateModel(
            name="Contacturgences",
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
                ("Qualite", models.CharField(max_length=100, null=True)),
                ("Nom", models.CharField(max_length=100, null=True)),
                ("Prenoms", models.CharField(max_length=250, null=True)),
                (
                    "Etudiant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.etudiants",
                    ),
                ),
            ],
        ),
    ]
