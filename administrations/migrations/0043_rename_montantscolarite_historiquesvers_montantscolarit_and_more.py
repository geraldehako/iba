# Generated by Django 4.1.7 on 2023-07-07 19:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "administrations",
            "0042_rename_montantscolarité_historiquesvers_montantscolarite_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="historiquesvers",
            old_name="Montantscolarite",
            new_name="Montantscolarit",
        ),
        migrations.RemoveField(
            model_name="historiquesvers",
            name="Montantverse",
        ),
    ]