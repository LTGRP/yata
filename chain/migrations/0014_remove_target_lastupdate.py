# Generated by Django 2.0.5 on 2018-10-31 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0013_target_lastupdatets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='lastUpdate',
        ),
    ]