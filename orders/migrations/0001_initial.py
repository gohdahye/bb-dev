# Generated by Django 4.2.4 on 2023-08-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("item", models.CharField(max_length=100)),
                ("quantity", models.PositiveIntegerField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
