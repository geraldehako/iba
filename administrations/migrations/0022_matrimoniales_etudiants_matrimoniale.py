# Generated by Django 4.1.7 on 2023-06-14 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("administrations", "0021_alter_moyennes_total"),
    ]

    operations = [
        migrations.CreateModel(
            name="Matrimoniales",
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
                ("Matrimoniale", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="etudiants",
            name="Matrimoniale",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="administrations.matrimoniales",
            ),
        ),
    ]