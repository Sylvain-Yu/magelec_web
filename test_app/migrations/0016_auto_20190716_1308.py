# Generated by Django 2.2.3 on 2019-07-16 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0015_auto_20190716_0848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='motor',
            options={'ordering': ['c_time'], 'verbose_name': '电机', 'verbose_name_plural': '电机数据关系集'},
        ),
    ]