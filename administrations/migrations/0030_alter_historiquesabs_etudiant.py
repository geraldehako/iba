# Generated by Django 4.1.7 on 2023-06-28 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("administrations", "0029_rename_heurefin_historiquesabs_heurefin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historiquesabs",
            name="Etudiant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.etudiants",
            ),
        ),
    ]
