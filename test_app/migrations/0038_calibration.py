# Generated by Django 2.2.3 on 2019-08-23 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0037_continuous'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calibration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_temperature', models.FloatField()),
                ('room_humidity', models.FloatField()),
                ('speed_point', models.IntegerField()),
                ('u_phase_voltage', models.FloatField()),
                ('v_phase_voltage', models.FloatField()),
                ('w_phase_voltage', models.FloatField()),
                ('Average_3phase_voltage', models.FloatField()),
                ('uv_phase_voltage', models.FloatField()),
                ('vw_phase_voltage', models.FloatField()),
                ('wu_phase_voltage', models.FloatField()),
                ('Average_3phase2phase_voltage', models.FloatField()),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('ke', models.FloatField()),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('motorinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.MotorInfo')),
            ],
            options={
                'verbose_name': '反电动势测量',
                'verbose_name_plural': '反电动势测量',
                'ordering': ['-c_time'],
            },
        ),
    ]