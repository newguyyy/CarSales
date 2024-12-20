# Generated by Django 5.1.4 on 2024-12-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                (
                    "Color",
                    models.CharField(
                        choices=[
                            ("Red", "Red"),
                            ("Blue", "Blue"),
                            ("Black", "Black"),
                            ("White", "White"),
                            ("Yellow", "Yellow"),
                            ("Green", "Green"),
                        ],
                        max_length=20,
                    ),
                ),
                ("InputPrice", models.FloatField()),
                ("OutputPrice", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("Name", models.CharField(max_length=20)),
                ("Sex", models.CharField(max_length=20)),
                ("Age", models.IntegerField()),
                ("Phone", models.CharField(max_length=20)),
                ("Native_Addr", models.CharField(max_length=20)),
                ("Salary", models.FloatField()),
                ("Position", models.CharField(max_length=20)),
            ],
        ),
    ]
