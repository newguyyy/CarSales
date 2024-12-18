# Generated by Django 5.1.4 on 2024-12-18 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Basic", "0001_squashed_0003_alter_car_name"),
        ("Output", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="Car_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="Order_Cars",
                to="Basic.car",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="Client_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="Order_Clients",
                to="Output.client",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="Staff_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="Order_Staffs",
                to="Basic.staff",
            ),
        ),
    ]