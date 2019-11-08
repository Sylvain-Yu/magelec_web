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
    list_display = ['motor_PN','motor_model','motor_code','speed','passornot','c_time','comment']
    search_fields = ['motor_PN','motor_model','motor_code']
    empty_value_display = '-空白-'
    list_per_page = 50
    date_hierarchy = 'c_time'

class TorqueVsCurrentInfo(admin.ModelAdmin):
    list_display = ['motor_PN','motor_model','motor_code','speed_point','rotate_direction','control_mode','c_time','comment']
    empty_value_display = '-空白-'
    search_fields = ['motor_PN','motor_model','motor_code']
    list_per_page = 50
    date_hierarchy = 'c_time'

class ShortCircuitInfo(admin.ModelAdmin):
    list_display = ['motor_PN','motor_model','motor_code','speed_point','c_time','comment']
    empty_value_display = '-空白-'
    search_fields = ['motor_PN','motor_model','motor_code']
    list_per_page = 50
    date_hierarchy = 'c_time'

class InsulationInfo(admin.ModelAdmin):
    list_display = ['motor_PN','motor_model','motor_code','c_time','comment']
    empty_value_display = '-空白-'
    search_fields = ['motor_PN','motor_model','motor_code']
    list_per_page = 50
    date_hierarchy = 'c_time'

class ContinuousInfo(admin.ModelAdmin):
    list_display = ['motor_PN','motor_model','motor_code','c_time','comment']
    empty_value_display = '-空白-'
    search_fields = ['motor_PN','motor_model','motor_code']
    list_per_page = 50
    date_hierarchy = 'c_time'

class BEMF_Info(admin.ModelAdmin):
    list_display = ['motor_PN','motor_model','motor_code','c_time','comment']
    empty_value_display = '-空白-'
    search_fields = ['motor_PN','motor_model','motor_code']
    list_per_page = 50
    date_hierarchy = 'c_time'

class CalibrationInfo(admin.ModelAdmin):
    list_display = ['motor_PN','motor_model','motor_code','c_time','comment']
    search_fields = ['motor_PN','motor_model','motor_code']
    empty_value_display = '-空白-'
    list_per_page = 50
    date_hierarchy = 'c_time'

class TestDataInfo(admin.ModelAdmin):
    list_display = ['motor_PN','motor_model','motor_code','c_time','comment']
    search_fields = ['motor_PN','motor_model','motor_code']
    empty_value_display = '-空白-'
    list_per_page = 50
    date_hierarchy = 'c_time'

admin.site.site_header = 'MAGELEC 信息管理后台'
admin.site.site_title = 'MAGELEC'
admin.site.register(models.MotorInfo,MotorSimpleInfo)
admin.site.register(models.HighSpeed,HighSpeedInfo)
admin.site.register(models.CurrentVsTorque,TorqueVsCurrentInfo)
admin.site.register(models.ShortCircuit,ShortCircuitInfo)
admin.site.register(models.Insulation,InsulationInfo)
admin.site.register(models.Continuous,ContinuousInfo)
admin.site.register(models.BEMF,BEMF_Info)
admin.site.register(models.Calibration,CalibrationInfo)
admin.site.register(models.TestData,TestDataInfo)
