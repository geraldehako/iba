# Generated by Django 4.1.7 on 2023-03-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ecoles",
            name="image",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
    ]