# Generated by Django 5.1.1 on 2024-11-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0016_alter_player_main_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]