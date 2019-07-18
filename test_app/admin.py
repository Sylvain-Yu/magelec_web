from django.contrib import admin
from . import models
# Register your models here.

class MotorSimpleInfo(admin.ModelAdmin):
    list_display = ['motor_PN','motor_model','motor_code','c_time','modify_time','comment']
    search_fields = ['motor_PN','motor_model','motor_code']
    date_hierarchy = 'c_time'
    list_per_page = 50
    empty_value_display = '-空白-'
    list_filter = ['motor_PN','motor_model']

class HighSpeedInfo(admin.ModelAdmin):
    list_display = ['speed','passornot','c_time','comment']
    empty_value_display = '-空白-'
    date_hierarchy = 'c_time'

class TorqueVsCurrentInfo(admin.ModelAdmin):
    list_display = ['speed_point','rotate_direction','control_mode','c_time','comment']
    empty_value_display = '-空白-'
    date_hierarchy = 'c_time'


admin.site.site_header = 'MAGELEC 信息管理后台'
admin.site.site_title = 'MAGELEC'
admin.site.register(models.MotorInfo,MotorSimpleInfo)
admin.site.register(models.HighSpeed,HighSpeedInfo)
admin.site.register(models.CurrentVsTorque,TorqueVsCurrentInfo)
