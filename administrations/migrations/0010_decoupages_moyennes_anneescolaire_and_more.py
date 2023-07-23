# Generated by Django 4.1.7 on 2023-03-24 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administrations", "0009_rename_note_notes"),
    ]

    operations = [
        migrations.CreateModel(
            name="Decoupages",
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
                ("Decoupage", models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name="moyennes",
            name="Anneescolaire",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.anneescolaires",
            ),
        ),
        migrations.AddField(
            model_name="notes",
            name="Anneescolaire",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.anneescolaires",
            ),
        ),
        migrations.AddField(
            model_name="moyennes",
            name="Decoupage",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.decoupages",
            ),
        ),
        migrations.AddField(
            model_name="notes",
            name="Decoupage",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.decoupages",
            ),
        ),
    ]
