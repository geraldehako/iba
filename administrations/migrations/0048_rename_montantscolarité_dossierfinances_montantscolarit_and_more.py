# Generated by Django 4.1.7 on 2023-07-07 19:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("administrations", "0047_alter_dossierscolaires_matrimoniale"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dossierfinances",
            old_name="Montantscolarité",
            new_name="Montantscolarit",
        ),
        migrations.RenameField(
            model_name="dossierfinances",
            old_name="Montantversé",
            new_name="Montantvers",
        ),
    ]
