# Generated by Django 2.2.3 on 2019-08-02 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0036_auto_20190801_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continuous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_mode', models.CharField(choices=[('Traction_Torque', '扭矩模式_主转'), ('Traction_Speed', '转速模式_主转'), ('Generation_Torque', '扭矩模式_跟转'), ('Generation_Speed', '转速模式_跟转')], max_length=32)),
                ('rotate_direction', models.CharField(choices=[('Positive', '正转'), ('Negitive', '反转')], max_length=32)),
                ('speed_point', models.IntegerField()),
                ('temperature_limit', models.IntegerField()),
                ('env_temperature', models.FloatField()),
                ('cooling_type', models.CharField(choices=[('Liquid cooling', '冷却液'), ('Air Cooling', '风冷')], max_length=32)),
                ('cooling_flow', models.FloatField()),
                ('cooling_temperature', models.FloatField()),
                ('BEMF_before_1000rpm', models.FloatField()),
                ('temperature_before_BEMF', models.FloatField()),
                ('BEMF_after_1000rpm', models.FloatField()),
                ('temperature_after_BEMF', models.FloatField()),
                ('RTD1_stable', models.FloatField()),
                ('RTD2_stable', models.FloatField()),
                ('torque_command', models.FloatField()),
                ('torque_measured', models.FloatField()),
                ('dc_bus_voltage', models.FloatField()),
                ('dc_current', models.FloatField()),
                ('voltage_ph2n', models.FloatField()),
                ('f_voltage_ph2n', models.FloatField()),
                ('current_ph2n', models.FloatField()),
                ('f_current_ph2n', models.FloatField()),
                ('power', models.FloatField()),
                ('f_power', models.FloatField()),
                ('pf', models.FloatField()),
                ('f_pf', models.FloatField()),
                ('motor_efficiency', models.FloatField()),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('motorinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.MotorInfo')),
            ],
            options={
                'verbose_name': '连续试验',
                'verbose_name_plural': '连续试验',
                'ordering': ['-c_time'],
            },
        ),
    ]