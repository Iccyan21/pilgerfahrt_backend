# Generated by Django 4.1.7 on 2023-06-28 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0004_rename_amineid_anime_anineid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="anime", old_name="anineid", new_name="animeid",
        ),
    ]
