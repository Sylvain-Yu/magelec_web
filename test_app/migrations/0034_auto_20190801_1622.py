# Generated by Django 2.2.3 on 2019-08-01 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0033_shortcircuit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortcircuit',
            name='deviation',
        ),
        migrations.RemoveField(
            model_name='shortcircuit',
            name='f_deviation',
        ),
    ]
