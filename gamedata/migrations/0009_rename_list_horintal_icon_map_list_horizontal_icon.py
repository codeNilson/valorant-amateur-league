# Generated by Django 5.1.1 on 2024-09-23 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamedata', '0008_agent_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='list_horintal_icon',
            new_name='list_horizontal_icon',
        ),
    ]