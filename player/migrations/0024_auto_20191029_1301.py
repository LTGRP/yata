# Generated by Django 2.0.5 on 2019-10-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0023_playerdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerdata',
            name='nDay',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerdata',
            name='nHour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playerdata',
            name='nMonth',
            field=models.IntegerField(default=0),
        ),
    ]
