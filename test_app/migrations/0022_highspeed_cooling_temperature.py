# Generated by Django 2.2.3 on 2019-07-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0021_highspeed_rotate_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='highspeed',
            name='cooling_temperature',
            field=models.FloatField(default='23'),
            preserve_default=False,
        ),
    ]
