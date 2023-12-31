# Generated by Django 4.1.7 on 2023-07-04 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("administrations", "0033_avis_postes_services_personnels_missions_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="personnels",
            name="Matrimoniale",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.matrimoniales",
            ),
        ),
        migrations.AddField(
            model_name="personnels",
            name="Sexe",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.genres",
            ),
        ),
    ]
