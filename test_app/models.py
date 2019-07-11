from django.db import models
# Create your models here.
class MotorInfo(models.Model):
    motormodel_choice = (('M17P3-S-18AXYY','M17P3-S-18AXYY'),
        ('M24P4','M24P4'),
        )
    motor_PN = models.CharField(max_length= 32)
    motor_model = models.CharField(max_length= 32, choices= motormodel_choice)
    motor_code = models.CharField(max_length= 32)
    tester_list = (('Leon Chen','陈晓文'),
        ('Tiegen Ji','季铁根'),
        ('Sylvain Yu','郁松林'),
        ('Jiliang Hong','小洪'),
        ('Charles Li','小李'),
        ('Brant Miao','苗强')
        )
    tester1 = models.CharField(max_length= 32, choices= tester_list)
    tester2 = models.CharField(max_length= 32, choices= tester_list)
    ambient_temperature = models.FloatField()
    ambient_humidity = models.FloatField()
    c_time = models.DateTimeField(auto_now_add=True)
    highspeed = models.ForeignKey('HighSpeed',on_delete = models.CASCADE)

    class Meta:
        ordering = ['c_time']
        verbose_name = "电机信息"
        verbose_name_plural = "电机信息"

    def __str__(self):
        return self.motor_model +' '+ self.motor_code
    

class HighSpeed(models.Model):
    speed = models.IntegerField()
    run_time = models.DurationField()
    RTD1_start_temperature = models.FloatField()
    RTD2_start_temperature = models.FloatField()
    RTD1_end_temperature = models.FloatField()
    RTD2_end_temperature = models.FloatField()
    passornot = models.BooleanField()
    c_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['c_time']
        verbose_name = "高转速试验"
        verbose_name_plural = "高转速试验"

    def __str__(self):
        return 'processing'
    