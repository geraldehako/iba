# Generated by Django 4.1.7 on 2023-07-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administrations", "0034_personnels_matrimoniale_personnels_sexe"),
    ]

    operations = [
        migrations.AddField(
            model_name="personnels",
            name="Statut",
            field=models.CharField(max_length=15, null=True),
        ),
    ]
