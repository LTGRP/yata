# Generated by Django 2.0.5 on 2019-05-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0045_faction_posteropt'),
    ]

    operations = [
        migrations.AddField(
            model_name='chain',
            name='lastUpdate',
            field=models.IntegerField(default=0),
        ),
    ]