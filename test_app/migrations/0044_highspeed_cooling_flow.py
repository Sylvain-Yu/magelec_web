# Generated by Django 2.2.3 on 2019-08-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0043_auto_20190827_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='highspeed',
            name='cooling_flow',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
    ]
