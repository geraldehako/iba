# Generated by Django 4.1.7 on 2023-03-25 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administrations", "0012_statutdecoups_decoupages_statutdecoup"),
    ]

    operations = [
        migrations.AddField(
            model_name="notes",
            name="Salle",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.salles",
            ),
        ),
    ]
