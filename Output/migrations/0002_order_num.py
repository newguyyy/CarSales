# Generated by Django 5.1.4 on 2024-12-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Output", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="num",
            field=models.IntegerField(default="1"),
        ),
    ]