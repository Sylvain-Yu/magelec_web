# Generated by Django 2.2.3 on 2019-08-27 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0042_calibration_gamma_ajust_x_10'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calibration',
            old_name='Gamma_Ajust_x_10',
            new_name='Gamma_Adjust_x_10',
        ),
    ]
