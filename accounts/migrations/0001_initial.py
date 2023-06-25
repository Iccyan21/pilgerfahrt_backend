# Generated by Django 4.1.7 on 2023-06-23 07:08

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                    "userid",
                    models.CharField(max_length=15, unique=True, verbose_name="UserID"),
                ),
                (
                    "name",
                    models.CharField(max_length=32, unique=True, verbose_name="name"),
                ),
                ("email", models.EmailField(max_length=32)),
                (
                    "introduction",
                    models.CharField(max_length=1024, verbose_name="自己紹介"),
                ),
                ("password", models.CharField(max_length=256)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="AccessToken",
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
                ("token", models.CharField(max_length=40)),
                (
                    "access_datetime",
                    models.DateTimeField(default=accounts.models.in_30_days),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="accounts.user"
                    ),
                ),
            ],
        ),
    ]
