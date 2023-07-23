# Generated by Django 4.1.7 on 2023-03-27 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "administrations",
            "0017_enseignants_user_alter_enseignants_matricule_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="ecoles",
            name="image",
            field=models.ImageField(null=True, upload_to="Images/Photos/ecole"),
        ),
        migrations.CreateModel(
            name="Documents",
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
                ("Title", models.CharField(max_length=255)),
                ("File", models.FileField(upload_to="Documents/Pedagogie/Cours")),
                (
                    "Anneescolaire",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.anneescolaires",
                    ),
                ),
                (
                    "Cours",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.matieres",
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
                (
                    "Typematiere",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrations.typematieres",
                    ),
                ),
            ],
        ),
    ]