# Generated by Django 2.2.3 on 2019-08-01 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0034_auto_20190801_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resistance_15s', models.FloatField()),
                ('resistance_30s', models.FloatField()),
                ('temperature_measured', models.FloatField()),
                ('rtd1', models.FloatField()),
                ('rtd2', models.FloatField()),
                ('room_temperature', models.FloatField()),
                ('room_humidity', models.FloatField()),
                ('winding_phase_u_v', models.FloatField()),
                ('winding_phase_v_w', models.FloatField()),
                ('winding_phase_u_w', models.FloatField()),
                ('insulation_voltage', models.IntegerField()),
                ('insulation_resistance', models.FloatField()),
                ('hipot_voltage', models.IntegerField()),
                ('hipot_resistance', models.FloatField()),
                ('recorder', models.CharField(blank=True, max_length=32, null=True)),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('motorinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.MotorInfo')),
            ],
            options={
                'verbose_name': '绝缘测试',
                'verbose_name_plural': '绝缘测试',
                'ordering': ['-c_time'],
            },
        ),
    ]
