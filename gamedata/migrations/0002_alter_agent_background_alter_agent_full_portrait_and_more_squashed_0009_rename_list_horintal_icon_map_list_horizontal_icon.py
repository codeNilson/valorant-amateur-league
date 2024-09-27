# Generated by Django 5.1.1 on 2024-09-26 12:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gamedata", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agent",
            name="background",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="agent",
            name="full_portrait",
            field=models.CharField(default="delete", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="agent",
            name="small_icon",
            field=models.CharField(default="oi", max_length=255),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="tier",
            name="uuid",
        ),
        migrations.AlterField(
            model_name="map",
            name="display_icon",
            field=models.CharField(default="oi", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="map",
            name="list_vertical_icon",
            field=models.CharField(default="oi", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="map",
            name="splash",
            field=models.CharField(default="oi", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tier",
            name="tier",
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name="role",
            name="icon",
            field=models.CharField(default="Oi", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="agent",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.RemoveField(
            model_name="agent",
            name="icon",
        ),
        migrations.AddField(
            model_name="agent",
            name="icon",
            field=models.CharField(default="oi", max_length=255),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name="map",
            old_name="list_horintal_icon",
            new_name="list_horizontal_icon",
        ),
        migrations.AlterField(
            model_name="map",
            name="list_horizontal_icon",
            field=models.CharField(default="oi", max_length=255),
        ),
    ]