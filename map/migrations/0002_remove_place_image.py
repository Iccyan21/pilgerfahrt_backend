# Generated by Django 4.1.7 on 2023-06-24 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="place", name="image",),
    ]
