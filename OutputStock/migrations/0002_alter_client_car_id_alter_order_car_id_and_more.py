# Generated by Django 5.1.3 on 2024-12-12 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BasicInformaiton", "0001_initial"),
        ("OutputStock", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="Car_id",
            field=models.ManyToManyField(
                through="OutputStock.Order", to="BasicInformaiton.car"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="Car_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="BasicInformaiton.car",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="Staff_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="BasicInformaiton.staff",
            ),
        ),
    ]
