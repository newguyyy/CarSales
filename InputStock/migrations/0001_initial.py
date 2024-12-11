# Generated by Django 5.1.3 on 2024-12-11 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Stock", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car_Supplier",
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
                ("Num", models.IntegerField()),
                ("Date", models.DateField()),
                ("TotalPrice", models.FloatField()),
                (
                    "Car_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="Stock.car"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
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
                ("Phone", models.CharField(max_length=20)),
                ("Addr", models.CharField(max_length=20)),
                (
                    "Car_id",
                    models.ManyToManyField(
                        through="InputStock.Car_Supplier", to="Stock.car"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="car_supplier",
            name="Supplier_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="InputStock.supplier"
            ),
        ),
    ]
