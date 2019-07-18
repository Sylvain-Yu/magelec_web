from django.db import models
from login_app.models import User
# Create your models here.


class MotorInfo(models.Model):
    motor_PN = models.CharField(max_length=32)
    motor_model = models.CharField(max_length=32)
    motor_code = models.CharField(max_length=32)
    tester_list = (('Leon Chen', '陈晓文'),
                   ('Tiegen Ji', '季铁根'),
                   ('Sylvain Yu', '郁松林'),
                   ('Jiliang Hong', '洪继良'),
                   ('Charles Li', '李文昌'),
                   ('Brant Miao', '苗强'),
                   ('others', '其他'),
                   )
    tester1 = models.CharField(max_length=32, choices=tester_list)
    tester2 = models.CharField(max_length=32, choices=tester_list)
    ambient_temperature = models.FloatField()
    ambient_humidity = models.FloatField()
    motor_poles = models.IntegerField()
    resolver_poles = models.IntegerField()
    inverter_type_list = (('RMS PM250DZ', 'RMS PM250DZ'),
                          ('RMS PM100', 'RMS PM100'),
                          ('EMSISO EM500', 'EMSISO EM500'),
                          ('EMSISO EM100', 'EMSISO EM100'),
                          ('EMSISO EM200', 'EMSISO EM200'),
                          ('unknown', '其他'),
                          )
    inverter_type = models.CharField(max_length=32, choices=inverter_type_list)
    inverter_serial = models.CharField(max_length=32)
    phase_connection_list = (('UVW to ABC', 'UVW to ABC'),
                             ('UWV to ABC', 'UWV to ABC'),
                             )
    phase_connection = models.CharField(
        max_length=32, choices=phase_connection_list)
    motor_type_options_eeprom = models.IntegerField()
    forward_direction_list = (('clockwise', '顺时针'),
                              ('anti-clockwise', '逆时针'),
                              )
    forward_direction = models.CharField(
        max_length=32, choices=forward_direction_list)
    comment = models.CharField(max_length=128, null=True, blank=True)
    c_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    recorder = models.ForeignKey(User,on_delete = models.SET_NULL,null= True)

    class Meta:
        ordering = ['-c_time']
        verbose_name = "电机信息"
        verbose_name_plural = "电机信息"

    def __str__(self):
        if self.comment:
            return self.motor_PN + ' ' + self.motor_model + ' ' + \
                self.motor_code+' | Remark: ' + self.comment
        else:
            return self.motor_PN + ' ' + self.motor_model + ' ' + self.motor_code


class HighSpeed(models.Model):
    speed = models.IntegerField()
    run_time = models.DurationField()
    forward_direction_list = (('Positive', '正转'),
                              ('Negitive', '反转'),
                              )
    rotate_direction = models.CharField(
        max_length=32, choices=forward_direction_list)
    RTD1_start_temperature = models.FloatField()
    RTD2_start_temperature = models.FloatField()
    RTD1_end_temperature = models.FloatField()
    RTD2_end_temperature = models.FloatField()
    cooling_temperature = models.FloatField()
    passornot = models.BooleanField()
    comment = models.CharField(max_length=128, null=True, blank=True)
    c_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    motorinfo = models.ForeignKey(MotorInfo,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-c_time']
        verbose_name = "高转速试验"
        verbose_name_plural = "高转速试验"

    def __str__(self):
        if self.comment:
            return str(self.speed) + 'rpm_' + str(self.c_time)+' | Remark: ' + self.comment
        else:
            return str(self.speed) + 'rpm_' + str(self.c_time)


class CurrentVsTorque(models.Model):
    speed_point = models.IntegerField()
    current_target = models.IntegerField(null=True)
    forward_direction_list = (('Positive', '正转'),
                              ('Negitive', '反转'),
                              )
    rotate_direction = models.CharField(
        max_length=32, choices=forward_direction_list)
    control_mode_list = (('Traction_Torque', '扭矩模式_主转'),
                         ('Traction_Speed', '转速模式_主转'),
                         ('Generation_Torque', '扭矩模式_跟转'),
                         ('Generation_Speed', '转速模式_跟转'),
                         )
    control_mode = models.CharField(max_length=32, choices=control_mode_list)
    cooling_type_list = (('Liquid cooling', '冷却液'),
                         ('Air Cooling', '风冷'),
                         )
    cooling_type = models.CharField(max_length=32, choices=cooling_type_list)
    cooling_flow = models.FloatField()
    cooling_temperature = models.FloatField()
    winding_temperature_min = models.FloatField()
    winding_temperature_max = models.FloatField()
    dc_bus_voltage = models.IntegerField()
    temperature_measured = models.FloatField(null=True)
    phase_current_measured = models.FloatField(null=True)
    torque_command = models.IntegerField(null=True)
    torque_measured = models.IntegerField(null=True)
    Kt = models.FloatField(null=True)
    Ke = models.FloatField(null=True)
    comment = models.CharField(max_length=128, null=True, blank=True)
    c_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-c_time']
        verbose_name = "电特性试验"
        verbose_name_plural = "电特性试验"

    def __str__(self):
        return str(self.c_time)
