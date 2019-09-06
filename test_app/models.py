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
                          ('EMSISO EM250', 'EMSISO EM250'),
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
    motor_PN = models.CharField(max_length=32)
    motor_model = models.CharField(max_length=32)
    motor_code = models.CharField(max_length=32)
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
    cooling_flow = models.FloatField()
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
            return self.motor_PN + ' ' + self.motor_model + ' ' + \
                self.motor_code +' ' +str(self.speed) + ' | Remark: ' + self.comment
        else:
            return self.motor_PN + ' ' + self.motor_model + ' ' + self.motor_code\
             + ' ' + str(self.speed)


class CurrentVsTorque(models.Model):
    motor_PN = models.CharField(max_length=32)
    motor_model = models.CharField(max_length=32)
    motor_code = models.CharField(max_length=32)
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
    motorinfo = models.ForeignKey(MotorInfo,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-c_time']
        verbose_name = "电特性试验"
        verbose_name_plural = "电特性试验"

    def __str__(self):
        if self.comment:
            return self.motor_PN + ' ' + self.motor_model + ' ' + \
                self.motor_code +' ' +str(self.speed_point) + ' | Remark: ' + self.comment
        else:
            return self.motor_PN + ' ' + self.motor_model + ' ' + self.motor_code\
             + ' ' + str(self.speed_point)

class ShortCircuit(models.Model):
    motor_PN = models.CharField(max_length=32)
    motor_model = models.CharField(max_length=32)
    motor_code = models.CharField(max_length=32)
    speed_point = models.IntegerField()
    cooling_temperature = models.FloatField()
    winding_temperature_min = models.FloatField()
    winding_temperature_max = models.FloatField()
    env_temperature = models.FloatField()
    env_humidity = models.FloatField()
    forward_direction_list = (('Positive', '正转'),
                              ('Negitive', '反转'),
                              )
    rotate_direction = models.CharField(
        max_length=32, choices=forward_direction_list)
    u_phase_current = models.FloatField()
    v_phase_current = models.FloatField()
    w_phase_current = models.FloatField()
    average_phase_current = models.FloatField()
    u_phase_f_current = models.FloatField()
    v_phase_f_current = models.FloatField()
    w_phase_f_current = models.FloatField()
    average_phase_f_current = models.FloatField()
    torque_measured = models.FloatField()
    temperature_measured = models.FloatField()
    comment = models.CharField(max_length=128, null=True, blank=True)
    c_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    motorinfo = models.ForeignKey(MotorInfo,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-c_time']
        verbose_name = "短路试验"
        verbose_name_plural = "短路试验"

    def __str__(self):
        if self.comment:
            return self.motor_PN + ' ' + self.motor_model + ' ' + \
                self.motor_code +' ' +str(self.speed_point) + ' | Remark: ' + self.comment
        else:
            return self.motor_PN + ' ' + self.motor_model + ' ' + self.motor_code\
             + ' ' + str(self.speed_point)

class Insulation(models.Model):
    motor_PN = models.CharField(max_length=32)
    motor_model = models.CharField(max_length=32)
    motor_code = models.CharField(max_length=32)
    resistance_15s = models.FloatField()
    resistance_60s = models.FloatField()
    temperature_measured = models.FloatField()
    rtd1 = models.FloatField()
    rtd2 = models.FloatField()
    room_temperature = models.FloatField()
    room_humidity = models.FloatField()
    winding_phase_u_v = models.FloatField()
    winding_phase_v_w = models.FloatField()
    winding_phase_u_w = models.FloatField()
    insulation_voltage = models.IntegerField()
    insulation_resistance = models.FloatField()
    hipot_voltage = models.IntegerField()
    hipot_resistance= models.FloatField()
    recorder = models.CharField(max_length=32,null = True,blank = True)
    comment = models.CharField(max_length=128, null=True, blank=True)
    c_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    motorinfo = models.ForeignKey(MotorInfo,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-c_time']
        verbose_name = "绝缘测试"
        verbose_name_plural = "绝缘测试"

    def __str__(self):
        if self.comment:
            return self.motor_PN + ' ' + self.motor_model + ' ' + \
                self.motor_code+' | Remark: ' + self.comment
        else:
            return self.motor_PN + ' ' + self.motor_model + ' ' + self.motor_code

class Continuous(models.Model):
    motor_PN = models.CharField(max_length=32)
    motor_model = models.CharField(max_length=32)
    motor_code = models.CharField(max_length=32)
    control_mode_list = (('Traction_Torque', '扭矩模式_主转'),
                     ('Traction_Speed', '转速模式_主转'),
                     ('Generation_Torque', '扭矩模式_跟转'),
                     ('Generation_Speed', '转速模式_跟转'),
                     )
    control_mode = models.CharField(max_length=32, choices=control_mode_list)
    forward_direction_list = (('Positive', '正转'),
                          ('Negitive', '反转'),
                          )
    rotate_direction = models.CharField(max_length=32, choices=forward_direction_list)
    speed_point = models.IntegerField()
    temperature_limit = models.IntegerField()
    env_temperature = models.FloatField()
    cooling_type_list = (('Liquid cooling', '冷却液'),
                     ('Air Cooling', '风冷'),
                     )
    cooling_type = models.CharField(max_length=32, choices=cooling_type_list)
    cooling_flow = models.FloatField()
    cooling_temperature = models.FloatField()
    BEMF_before_1000rpm = models.FloatField()
    temperature_before_BEMF = models.FloatField()
    BEMF_after_1000rpm = models.FloatField()
    temperature_after_BEMF = models.FloatField()
    RTD1_stable = models.FloatField()
    RTD2_stable = models.FloatField()
    torque_command = models.FloatField()
    torque_measured = models.FloatField()
    dc_bus_voltage = models.FloatField()
    dc_current = models.FloatField()
    voltage_ph2n = models.FloatField()
    f_voltage_ph2n = models.FloatField()
    current_ph2n = models.FloatField()
    f_current_ph2n = models.FloatField()
    power = models.FloatField()
    f_power = models.FloatField()
    pf = models.FloatField()
    f_pf = models.FloatField()
    motor_efficiency = models.FloatField()
    comment = models.CharField(max_length=128, null=True, blank=True)
    c_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    motorinfo = models.ForeignKey(MotorInfo,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-c_time']
        verbose_name = "连续试验"
        verbose_name_plural = "连续试验"

    def __str__(self):
        if self.comment:
            return self.motor_PN + ' ' + self.motor_model + ' ' + \
                self.motor_code +' ' +str(self.speed_point) + ' | Remark: ' + self.comment
        else:
            return self.motor_PN + ' ' + self.motor_model + ' ' + self.motor_code\
             + ' ' + str(self.speed_point)

class BEMF(models.Model):
    motor_PN = models.CharField(max_length=32)
    motor_model = models.CharField(max_length=32)
    motor_code = models.CharField(max_length=32)
    room_temperature = models.FloatField()
    room_humidity = models.FloatField()
    speed_point = models.IntegerField()
    u_phase_voltage = models.FloatField()
    v_phase_voltage = models.FloatField()
    w_phase_voltage = models.FloatField()
    Average_3phase_voltage = models.FloatField()
    uv_phase_voltage = models.FloatField()
    vw_phase_voltage = models.FloatField()
    wu_phase_voltage = models.FloatField()
    Average_3phase2phase_voltage = models.FloatField()
    ke = models.FloatField()
    comment = models.CharField(max_length=128, null=True, blank=True)
    c_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    motorinfo = models.ForeignKey(MotorInfo,on_delete=models.CASCADE)


    class Meta:
        ordering = ['-c_time']
        verbose_name = "反电动势测量"
        verbose_name_plural = "反电动势测量"

    def __str__(self):
        if self.comment:
            return self.motor_PN + ' ' + self.motor_model + ' ' + \
                self.motor_code +' ' +str(self.speed_point) + ' | Remark: ' + self.comment
        else:
            return self.motor_PN + ' ' + self.motor_model + ' ' + self.motor_code\
             + ' ' + str(self.speed_point)
        
class Calibration(models.Model):
    motor_PN = models.CharField(max_length=32)
    motor_model = models.CharField(max_length=32)
    motor_code = models.CharField(max_length=32)
    Stator_Resistance_EEPROM_x_10000 = models.IntegerField()
    Veh_Flux_EEPROM_web_x_1000 =  models.IntegerField()
    Ld_Lq_Const_EEPROM_uH = models.IntegerField()
    Kp_Current_EEPROM_x_1000 = models.IntegerField()
    Ki_Current_EEPROM_x_10000 = models.IntegerField()
    Gamma_Adjust_x_10 = models.IntegerField()
    comment = models.CharField(max_length=128, null=True, blank=True)
    c_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    motorinfo = models.ForeignKey(MotorInfo,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-c_time']
        verbose_name = "校准"
        verbose_name_plural = "校准"

    def __str__(self):
        if self.comment:
            return self.motor_PN + ' ' + self.motor_model + ' ' + \
                self.motor_code+' | Remark: ' + self.comment
        else:
            return self.motor_PN + ' ' + self.motor_model + ' ' + self.motor_code
