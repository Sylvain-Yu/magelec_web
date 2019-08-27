# Generated by Django 2.2.3 on 2019-08-23 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0039_auto_20190823_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calibration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Veh_Flux_EEPROM_web_x_1000', models.IntegerField()),
                ('Ld_Lq_Const_EEPROM_uH', models.IntegerField()),
                ('Kp_Current_EEPROM_x_1000', models.IntegerField()),
                ('Ki_Current_EEPROM_x_10000', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('motorinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.MotorInfo')),
            ],
            options={
                'verbose_name': '校准',
                'verbose_name_plural': '校准',
                'ordering': ['-c_time'],
            },
        ),
    ]
