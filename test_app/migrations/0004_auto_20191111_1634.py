# Generated by Django 2.2.3 on 2019-11-11 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20190906_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorinfo',
            name='inverter_type',
            field=models.CharField(choices=[('RMS PM250DZ', 'RMS PM250DZ'), ('RMS PM100', 'RMS PM100'), ('EMSISO EM500', 'EMSISO EM500'), ('EMSISO EM100', 'EMSISO EM100'), ('EMSISO EM200', 'EMSISO EM200'), ('EMSISO EM250', 'EMSISO EM250'), ('unknown', '其他')], max_length=32),
        ),
        migrations.CreateModel(
            name='Assemble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motor_PN', models.CharField(max_length=32)),
                ('motor_model', models.CharField(max_length=32)),
                ('motor_code', models.CharField(max_length=32)),
                ('Phase_diff', models.FloatField()),
                ('phase_Un', models.FloatField()),
                ('phase_Vn', models.FloatField()),
                ('phase_Wn', models.FloatField()),
                ('comment', models.CharField(blank=True, max_length=128, null=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('motorinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.MotorInfo')),
            ],
            options={
                'verbose_name': '装配信息',
                'verbose_name_plural': '装配信息',
                'ordering': ['-c_time'],
            },
        ),
    ]
