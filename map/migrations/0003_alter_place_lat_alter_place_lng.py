# Generated by Django 4.1.7 on 2023-06-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0002_remove_place_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="lat",
            field=models.DecimalField(
                decimal_places=6, max_digits=9, verbose_name="緯度"
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="lng",
            field=models.DecimalField(
                decimal_places=6, max_digits=10, verbose_name="経度"
            ),
        ),
    ]
