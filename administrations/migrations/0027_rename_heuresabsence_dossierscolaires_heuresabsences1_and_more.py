# Generated by Django 4.1.7 on 2023-06-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administrations", "0026_rename_prix_catalogues_prix"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dossierscolaires",
            old_name="Heuresabsence",
            new_name="HeuresabsenceS1",
        ),
        migrations.AddField(
            model_name="dossierscolaires",
            name="HeuresabsenceS2",
            field=models.IntegerField(default=0),
        ),
    ]
