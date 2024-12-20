# Generated by Django 5.1.4 on 2024-12-18 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Basic", "0001_squashed_0003_alter_car_name"),
        ("Stock", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car_stock",
            name="Car_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="Car_Stock_Cars",
                to="Basic.car",
            ),
        ),
        migrations.AlterField(
            model_name="car_stock",
            name="Stock_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="Car_Stock_Stocks",
                to="Stock.stock",
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="Staff_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="staffs",
                to="Basic.staff",
            ),
        ),
    ]
