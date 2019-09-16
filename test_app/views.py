from django.shortcuts import render, redirect, HttpResponse
from functools import wraps
from login_app import models as login_app_models
from . import models
from datetime import timedelta
import math
# Create your views here.

def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwarg):
        if request.session.get('is_login') == '1':
            return f(request,*arg,**kwarg)
        else:
            return redirect('login_app:index')
    return inner

def pass_info(f):
    @wraps(f)
    def inner(request,*arg,**kwarg):
        user_id1 = request.session.get('user_id')
        motor_id_text = request.session.get('motor_id')
        userobj = login_app_models.User.objects.filter(id = user_id1).first()
        motorinfoobj =models.MotorInfo.objects.filter(id=motor_id_text).first()
        # print(motorinfoobj)
        context = {'user':userobj,'motorinfoobj':motorinfoobj}
        return f(request,*arg,context)
    return inner


@check_login
@pass_info
def dataview(request,context):
    try:
        motorinfoobj = context['motorinfoobj']
        if motorinfoobj:
            motorhighspeedobj_list = motorinfoobj.highspeed_set.all()
            context['motorhighspeedobj_list'] = motorhighspeedobj_list
            motorcvtobj_list = motorinfoobj.currentvstorque_set.all()
            context['motorcvtobj_list'] = motorcvtobj_list
            motorscobj_list = motorinfoobj.shortcircuit_set.all()
            context['motorscobj_list'] = motorscobj_list
            motorinsulationobj_list = motorinfoobj.insulation_set.all()
            context['motorinsulationobj_list'] = motorinsulationobj_list
            motorbemfobj_list = motorinfoobj.bemf_set.all()
            # print(motorbemfobj_list)
            context['motorbemfobj_list'] = motorbemfobj_list
            motorcalibrateobj_list = motorinfoobj.calibration_set.all()
            context['motorcalibrateobj_list'] = motorcalibrateobj_list
            motorconti_list = motorinfoobj.continuous_set.all()
            context['motorcontiobj_list'] = motorconti_list
    except Exception as e:
        print(e)
    return render(request,'test_app/dataview.html',context)





@check_login
@pass_info
def motor_login(request,context):
    if request.method =='POST':
        motor_id = request.POST.get('motorindex')
        request.session['motor_id'] = motor_id
        # print(motor_id)
        return redirect('test_app:dataview')
    return HttpResponse('未能成功跳转，请联系管理员！')


@check_login
@pass_info
def index(request,context):
    return render(request,'test_app/index.html',context)


def motor_logout(request):
    request.session['motor_id'] = False
    return redirect('test_app:index')

@check_login
@pass_info
def shortcircuit(request,context):
    motorinfoobj = context['motorinfoobj']
    shortcircuitobj = models.ShortCircuit()
    context['forward_direction_list'] = shortcircuitobj.forward_direction_list
    try:
        context['cooling_temp'] = request.session.get('cooling_temp')
        context['env_temperature'] = request.session.get('env_temperature')
        context['env_humidity'] = request.session.get('env_humidity')
        context['cond_temp_min'] = request.session.get('cond_temp_min')
        context['cond_temp_max'] = request.session.get('cond_temp_max')
        if request.method =='POST' and motorinfoobj:
            # print(request.POST)
            shortcircuitobj.speed_point = request.POST.get('speed_point')
            shortcircuitobj.cooling_temperature = request.POST.get('cooling_temperature')
            shortcircuitobj.winding_temperature_min = request.POST.get('winding_temperature_min')
            shortcircuitobj.winding_temperature_max = request.POST.get('winding_temperature_max')
            shortcircuitobj.env_temperature = request.POST.get('env_temperature')
            shortcircuitobj.env_humidity = request.POST.get('env_humidity')
            shortcircuitobj.rotate_direction = request.POST.get('rotate_direction')
            shortcircuitobj.u_phase_current = request.POST.get('u_phase_current')
            shortcircuitobj.v_phase_current = request.POST.get('v_phase_current')
            shortcircuitobj.w_phase_current = request.POST.get('w_phase_current')
            shortcircuitobj.average_phase_current = (float(request.POST.get('u_phase_current'))+
            float(request.POST.get('v_phase_current')) +float(request.POST.get('w_phase_current')))/3
            shortcircuitobj.u_phase_f_current = request.POST.get('u_phase_f_current')
            shortcircuitobj.v_phase_f_current = request.POST.get('v_phase_f_current')
            shortcircuitobj.w_phase_f_current = request.POST.get('w_phase_f_current')
            shortcircuitobj.average_phase_f_current = (float(request.POST.get('u_phase_f_current'))+
            float(request.POST.get('v_phase_f_current'))+float(request.POST.get('w_phase_f_current')))/3
            shortcircuitobj.torque_measured = request.POST.get('torque_measured')
            shortcircuitobj.temperature_measured = request.POST.get('temperature_measured')
            shortcircuitobj.comment = request.POST.get('comment')
            shortcircuitobj.motorinfo = motorinfoobj
            shortcircuitobj.motor_PN = motorinfoobj.motor_PN
            shortcircuitobj.motor_model = motorinfoobj.motor_model
            shortcircuitobj.motor_code = motorinfoobj.motor_code
            shortcircuitobj.save()
            request.session['env_temperature'] = shortcircuitobj.env_temperature
            request.session['env_humidity'] = shortcircuitobj.env_humidity
            request.session['cond_temp_min'] = shortcircuitobj.winding_temperature_min
            request.session['cond_temp_max'] = shortcircuitobj.winding_temperature_max
            request.session['cooling_temp'] = shortcircuitobj.cooling_temperature
            return redirect('test_app:dataview')
    except Exception as e:
        print(e)
    return render(request,'test_app/shortcircuit.html',context)

@check_login
@pass_info
def continuous(request,context):
    motorinfoobj = context['motorinfoobj']
    continuousobj = models.Continuous()
    context['control_mode_list'] = continuousobj.control_mode_list
    context['forward_direction_list'] = continuousobj.forward_direction_list
    context['cooling_type_list'] = continuousobj.cooling_type_list
    context['cooling_temp'] = request.session.get('cooling_temp')
    context['cooling_flow'] = request.session.get('cooling_flow')
    context['dc_bus_voltage'] = request.session.get('dc_bus_voltage')
    context['cond_temp_max'] = request.session.get('cond_temp_max')
    try:
        if request.method == 'POST' and motorinfoobj:
            continuousobj.control_mode = request.POST.get('control_mode')
            continuousobj.rotate_direction = request.POST.get('rotate_direction')
            continuousobj.speed_point = request.POST.get('speed_point')
            continuousobj.temperature_limit = request.POST.get('temperature_limit')
            continuousobj.env_temperature = request.POST.get('env_temperature')
            continuousobj.cooling_type = request.POST.get('cooling_type')
            continuousobj.cooling_flow = request.POST.get('cooling_flow')
            continuousobj.cooling_temperature = request.POST.get('cooling_temperature')
            continuousobj.BEMF_before_1000rpm = request.POST.get('BEMF_before_1000rpm')
            continuousobj.temperature_before_BEMF = request.POST.get('temperature_before_BEMF')
            continuousobj.BEMF_after_1000rpm = request.POST.get('BEMF_after_1000rpm')
            continuousobj.temperature_after_BEMF = request.POST.get('temperature_after_BEMF')
            continuousobj.RTD1_stable = request.POST.get('RTD1_stable')
            continuousobj.RTD2_stable = request.POST.get('RTD2_stable')
            continuousobj.torque_command = request.POST.get('torque_command')
            continuousobj.torque_measured = request.POST.get('torque_measured')
            continuousobj.dc_bus_voltage = request.POST.get('dc_bus_voltage')
            continuousobj.dc_current = request.POST.get('dc_current')
            continuousobj.voltage_ph2n = request.POST.get('voltage_ph2n')
            continuousobj.f_voltage_ph2n = request.POST.get('f_voltage_ph2n')
            continuousobj.current_ph2n = request.POST.get('current_ph2n')
            continuousobj.f_current_ph2n = request.POST.get('f_current_ph2n')
            continuousobj.power = request.POST.get('power')
            continuousobj.f_power = request.POST.get('f_power')
            continuousobj.pf = request.POST.get('pf')
            continuousobj.f_pf = request.POST.get('f_pf')
            continuousobj.motor_efficiency = request.POST.get('motor_efficiency')
            continuousobj.comment = request.POST.get('comment')
            continuousobj.motorinfo = motorinfoobj
            continuousobj.motor_PN = motorinfoobj.motor_PN
            continuousobj.motor_model = motorinfoobj.motor_model
            continuousobj.motor_code = motorinfoobj.motor_code
            continuousobj.save()
            request.session['cooling_temp'] = continuousobj.cooling_temperature
            request.session['cooling_flow'] = continuousobj.cooling_flow
            request.session['dc_bus_voltage'] = continuousobj.dc_bus_voltage
            request.session['cond_temp_max'] = continuousobj.temperature_limit
            return redirect('test_app:dataview')
    except Exception as e:
        print(e)
    return render(request,'test_app/continuous.html',context)



@check_login
@pass_info
def insulation(request,context):
    motorinfoobj = context['motorinfoobj']
    insulationobj = models.Insulation()
    try:
        if request.method == 'POST' and motorinfoobj:
            insulationobj.resistance_15s = request.POST.get('resistance_15s')
            insulationobj.resistance_60s = request.POST.get('resistance_60s')
            insulationobj.temperature_measured = request.POST.get('temperature_measured')
            insulationobj.rtd1 = request.POST.get('RTD1')
            insulationobj.rtd2 = request.POST.get('RTD2')
            insulationobj.room_temperature = request.POST.get('room_temperature')
            insulationobj.room_humidity = request.POST.get('room_humidity')
            insulationobj.winding_phase_u_v = request.POST.get('winding_phase_u_v')
            insulationobj.winding_phase_v_w = request.POST.get('winding_phase_v_w')
            insulationobj.winding_phase_u_w = request.POST.get('winding_phase_u_w')
            insulationobj.insulation_voltage = request.POST.get('insulation_voltage')
            insulationobj.insulation_resistance = request.POST.get('insulation_resistance')
            insulationobj.hipot_voltage = request.POST.get('hipot_voltage')
            insulationobj.hipot_resistance = request.POST.get('hipot_resistance')
            insulationobj.comment = request.POST.get('comment')
            insulationobj.recorder = context['user']
            insulationobj.motorinfo = motorinfoobj
            insulationobj.motor_PN = motorinfoobj.motor_PN
            insulationobj.motor_model = motorinfoobj.motor_model
            insulationobj.motor_code = motorinfoobj.motor_code
            insulationobj.save()
            return redirect('test_app:dataview')
    except Exception as e:
        print(e)
    return render(request,'test_app/insulation.html',context)

@check_login
@pass_info
def currentvstorque(request,context):
    motorinfoobj = context['motorinfoobj']
    cvtobj = models.CurrentVsTorque()
    context['cooling_type_list'] = cvtobj.cooling_type_list
    context['forward_direction_list'] = cvtobj.forward_direction_list
    context['control_mode_list'] = cvtobj.control_mode_list
    context['cooling_temp'] = request.session.get('cooling_temp')
    context['cooling_flow'] = request.session.get('cooling_flow')
    context['dc_bus_voltage'] = request.session.get('dc_bus_voltage')
    context['cond_temp_min'] = request.session.get('cond_temp_min')
    context['cond_temp_max'] = request.session.get('cond_temp_max')
    try:
        if request.method =='POST' and motorinfoobj:
            cvtobj.speed_point = request.POST.get('speed_point')
            cvtobj.current_target = request.POST.get('current_target')
            cvtobj.rotate_direction = request.POST.get('rotate_direction')
            cvtobj.control_mode = request.POST.get('control_mode')
            cvtobj.cooling_type = request.POST.get('cooling_type')
            cvtobj.cooling_flow = request.POST.get('cooling_flow')
            cvtobj.cooling_temperature = request.POST.get('cooling_temperature')
            cvtobj.winding_temperature_min = request.POST.get('winding_temperature_min')
            cvtobj.winding_temperature_max = request.POST.get('winding_temperature_max')
            cvtobj.dc_bus_voltage = request.POST.get('dc_bus_voltage')
            cvtobj.temperature_measured = request.POST.get('temperature_measured')
            cvtobj.phase_current_measured = request.POST.get('phase_current_measured')
            cvtobj.torque_command = request.POST.get('torque_command')
            cvtobj.torque_measured = request.POST.get('torque_measured')
            phase_current_measured = float(request.POST.get('phase_current_measured'))
            torque_measured = float(request.POST.get('torque_command'))
            kt = torque_measured / phase_current_measured
            cvtobj.Kt = str(kt)
            cvtobj.Ke = str(kt/3**0.5)
            cvtobj.comment = request.POST.get('comment')
            cvtobj.motorinfo = motorinfoobj
            cvtobj.motor_PN = motorinfoobj.motor_PN
            cvtobj.motor_model = motorinfoobj.motor_model
            cvtobj.motor_code = motorinfoobj.motor_code
            cvtobj.save()
            request.session['dc_bus_voltage'] = cvtobj.dc_bus_voltage
            request.session['cond_temp_min'] = cvtobj.winding_temperature_min
            request.session['cond_temp_max'] = cvtobj.winding_temperature_max
            request.session['cooling_flow'] = cvtobj.cooling_flow
            request.session['cooling_temp'] = cvtobj.cooling_temperature
            return redirect('test_app:dataview')
    except Exception as e:
        print(e)
    return render(request,'test_app/currentvstorque.html',context)


@pass_info
@check_login
def highspeed(request,context):
    context['forward_direction_list'] = models.HighSpeed.forward_direction_list
    motorinfoobj = context['motorinfoobj']
    context['cooling_flow'] = request.session.get('cooling_flow')
    context['cooling_temp'] = request.session.get('cooling_temp')
    try:
        if request.method =='POST' and motorinfoobj:
            highspeedobj = models.HighSpeed()
            highspeedobj.speed = request.POST.get('speed')
            minutes,seconds = [ int(x) for x in request.POST.get('run_time').split(':')]
            highspeedobj.run_time = timedelta(seconds=seconds,minutes=minutes)
            highspeedobj.RTD1_start_temperature = request.POST.get('RTD1_start_temperature')
            highspeedobj.RTD2_start_temperature = request.POST.get('RTD2_start_temperature')
            highspeedobj.RTD1_end_temperature = request.POST.get('RTD1_end_temperature')
            highspeedobj.RTD2_end_temperature = request.POST.get('RTD2_end_temperature')
            highspeedobj.cooling_temperature = request.POST.get('cooling_temperature')
            highspeedobj.cooling_flow = request.POST.get('cooling_flow')
            highspeedobj.rotate_direction = request.POST.get('rotate_direction')
            highspeedobj.comment = request.POST.get('comment')
            if request.POST.get('passornot') == 'on':
                highspeedobj.passornot = True
            else:
                highspeedobj.passornot = False
            highspeedobj.motorinfo = motorinfoobj
            highspeedobj.motor_PN = motorinfoobj.motor_PN
            highspeedobj.motor_model = motorinfoobj.motor_model
            highspeedobj.motor_code = motorinfoobj.motor_code
            highspeedobj.save()
            request.session['cooling_temp'] = highspeedobj.cooling_temperature
            request.session['cooling_flow'] = highspeedobj.cooling_flow
            return redirect('test_app:dataview')
    except Exception as e:
        print(e)
    return render(request,'test_app/highspeed.html',context)



@pass_info
@check_login
def basic(request,context):
    context['testerlist'] =models.MotorInfo.tester_list
    context['phaseconnect'] =models.MotorInfo.phase_connection_list
    context['direction_list'] =models.MotorInfo.forward_direction_list
    context['inverter_type_list'] =models.MotorInfo.inverter_type_list
    if request.method == 'POST':
        try:
            motorinfo = models.MotorInfo()
            motor_PN = request.POST.get('motor_PN')
            motorinfo.motor_PN = motor_PN
            motor_model = request.POST.get('motor_model')
            motorinfo.motor_model = motor_model
            motor_code = request.POST.get('motor_code')
            motorinfo.motor_code = motor_code
            if motorinfo.motor_PN and motorinfo.motor_model and motorinfo.motor_code:
                motorinfo.tester1 = request.POST.get('tester1')
                motorinfo.tester2 = request.POST.get('tester2')
                motorinfo.ambient_temperature = request.POST.get('env_temperature')
                motorinfo.ambient_humidity = request.POST.get('env_humidity')
                motorinfo.motor_poles = request.POST.get('motor_poles')
                motorinfo.resolver_poles = request.POST.get('resolver_poles')
                motorinfo.motor_code = request.POST.get('motor_code')
                motorinfo.phase_connection = request.POST.get('phase_connection')
                motorinfo.forward_direction = request.POST.get('forward_direct')
                motorinfo.inverter_type = request.POST.get('inverter_type')
                motorinfo.inverter_serial = request.POST.get('inverter_serial')
                motor_type_options_eeprom = request.POST.get('eeprom')
                if motor_type_options_eeprom in ['34','50']:
                    motorinfo.motor_type_options_eeprom = request.POST.get('eeprom')
                else:
                    motorinfo.motor_type_options_eeprom = None
                motorinfo.comment = request.POST.get('comment')
                motorinfo.recorder = context['user']
                motorinfo.save()
                # 数据留存设置
                request.session['motor_id'] = motorinfo.id
                request.session['env_temperature'] = motorinfo.ambient_temperature
                request.session['env_humidity'] = motorinfo.ambient_humidity
                return redirect('test_app:dataview')
        except Exception as e:
            print(e)
    return render(request,'test_app/basic.html',context)

@check_login
@pass_info
def bemf(request,context):
    motorinfoobj = context['motorinfoobj']
    try:
        context['env_temperature'] = request.session.get('env_temperature')
        context['env_humidity'] = request.session.get('env_humidity')
        if request.method =='POST' and motorinfoobj:
            bemfobj = models.BEMF()
            bemfobj.room_temperature = request.POST.get('room_temperature')
            bemfobj.room_humidity = request.POST.get('room_humidity')
            speed_point = request.POST.get('speed_point')
            bemfobj.speed_point = speed_point
            u_phase_voltage = request.POST.get('u_phase_voltage')
            v_phase_voltage = request.POST.get('v_phase_voltage')
            w_phase_voltage = request.POST.get('w_phase_voltage')
            Average_3phase_voltage = str((float(u_phase_voltage) + \
                float(v_phase_voltage) + float(w_phase_voltage))/3)
            bemfobj.u_phase_voltage = u_phase_voltage
            bemfobj.v_phase_voltage = v_phase_voltage
            bemfobj.w_phase_voltage = w_phase_voltage
            bemfobj.Average_3phase_voltage = Average_3phase_voltage
            uv_phase_voltage = request.POST.get('uv_phase_voltage')
            vw_phase_voltage = request.POST.get('vw_phase_voltage')
            wu_phase_voltage = request.POST.get('wu_phase_voltage')
            Average_3phase2phase_voltage = str((float(uv_phase_voltage) + \
                float(vw_phase_voltage) + float(wu_phase_voltage))/3)
            bemfobj.uv_phase_voltage = uv_phase_voltage
            bemfobj.vw_phase_voltage = vw_phase_voltage
            bemfobj.wu_phase_voltage = wu_phase_voltage
            bemfobj.Average_3phase2phase_voltage = Average_3phase2phase_voltage
            bemfobj.ke = str((float(speed_point)/376.8)/float(Average_3phase2phase_voltage))
            bemfobj.comment = request.POST.get('comment')
            bemfobj.motorinfo = motorinfoobj
            bemfobj.motor_PN = motorinfoobj.motor_PN
            bemfobj.motor_model = motorinfoobj.motor_model
            bemfobj.motor_code = motorinfoobj.motor_code
            bemfobj.save()
            request.session['env_temperature'] = bemfobj.room_temperature
            request.session['env_humidity'] = bemfobj.room_humidity
            return redirect('test_app:dataview')
    except Exception as e:
        print(e)
    return render(request,'test_app/bemf.html',context)


@check_login
@pass_info
def calibrate(request,context):
    motorinfoobj = context['motorinfoobj']
    if motorinfoobj.insulation_set.all().first():
        insulationobj = motorinfoobj.insulation_set.all().first()
        uv = float(insulationobj.winding_phase_u_v)
        vw = float(insulationobj.winding_phase_v_w)
        wu = float(insulationobj.winding_phase_u_w)
        u = (wu + (uv - vw))/2
        v = (uv - u)
        w = (wu - u)
        _,winding_average = math.modf((u + v + w)*10/3)
        winding_average = str(int(winding_average))
        context['winding_average'] = winding_average

        if motorinfoobj.bemf_set.filter(speed_point = '1000').first():
            bemfobj = motorinfoobj.bemf_set.filter(speed_point = '1000').first()
            u_phase_voltage = float(bemfobj.u_phase_voltage)
            v_phase_voltage = float(bemfobj.v_phase_voltage)
            w_phase_voltage = float(bemfobj.w_phase_voltage)
            motor_elec_speed = float(bemfobj.speed_point) * math.pi * float(motorinfoobj.motor_poles)/60
            veh_flux = str(round(float(bemfobj.Average_3phase_voltage)* math.sqrt(2)/motor_elec_speed * 1000))
            context['veh_flux'] = veh_flux

            if motorinfoobj.shortcircuit_set.all().first():
                shortcircuitobj = motorinfoobj.shortcircuit_set.filter(speed_point= '1000').first()
                u_phase_current = float(shortcircuitobj.u_phase_current)
                v_phase_current = float(shortcircuitobj.v_phase_current)
                w_phase_current = float(shortcircuitobj.w_phase_current)
                # print(u_phase_voltage,u_phase_current,u,motor_elec_speed)
                inductance_U = math.sqrt((u_phase_voltage/u_phase_current)**2-(u/1000)**2)/motor_elec_speed
                inductance_V = math.sqrt((v_phase_voltage/v_phase_current)**2-(v/1000)**2)/motor_elec_speed
                inductance_W = math.sqrt((w_phase_voltage/w_phase_current)**2-(u/1000)**2)/motor_elec_speed
                # print(inductance_U)
                Ld_Lq_Const = round((inductance_U + inductance_V + inductance_W)*1000000/3)
                context['Ld_Lq_Const'] = Ld_Lq_Const
                w1 = int(winding_average)/10000/(Ld_Lq_Const/1000000)
                kp = (Ld_Lq_Const/1000000)*w1/(200/300)
                ki = kp * w1/12000
                Kp_Current = round(kp * 1000)
                Ki_Current = round(ki * 10000)
                context['Kp_Current'] = str(Kp_Current)
                context['Ki_Current'] = str(Ki_Current)
    try:
        if request.method =='POST' and motorinfoobj:
            calobj = models.Calibration()
            # print(calobj)
            # print(request.POST)
            calobj.Stator_Resistance_EEPROM_x_10000 = request.POST.get('Stator_Resistance_EEPROM_x10000')
            calobj.Veh_Flux_EEPROM_web_x_1000 = request.POST.get('Veh_Flux_EEPROM_x1000')
            calobj.Ld_Lq_Const_EEPROM_uH = request.POST.get('Ld_Lq_Const_EEPROM')
            calobj.Kp_Current_EEPROM_x_1000 = request.POST.get('Kp_Current_EEPROM_x1000')
            calobj.Ki_Current_EEPROM_x_10000 = request.POST.get('Ki_Current_EEPROM_x10000')
            calobj.Gamma_Adjust_x_10 = request.POST.get('Gamma_Adjust_x10')
            calobj.comment = request.POST.get('comment')
            calobj.motorinfo = motorinfoobj
            calobj.motor_PN = motorinfoobj.motor_PN
            calobj.motor_model = motorinfoobj.motor_model
            calobj.motor_code = motorinfoobj.motor_code
            calobj.save()
            return redirect('test_app:dataview')
    except Exception as e:
        print(e)
    return render(request,'test_app/calibrate.html',context)


@pass_info
@check_login
def efficiency(request,context):
    pass
    return render(request,'test_app/efficiency.html',context)


@pass_info
@check_login
def gamma(request,context):
    try:
        if request.method =='POST':
            gamma_ajust_now = request.POST.get('Gamma_Adjust_now')
            Delta_Resolver = request.POST.get('Delta_Resolver')
            value = float(gamma_ajust_now) - (900 - float(Delta_Resolver))
            # print(value)
            while True:
                if value > 1800:
                    value = value - 3600
                elif value < -1800:
                    value = value + 3600
                else:
                    break
            print(value)
            context['gamma_ajust_after'] = str(value)
            return render(request,'test_app/gamma.html',context)
    except Exception as e:
        print(e)
    return render(request,'test_app/gamma.html',context)



@pass_info
@check_login
def search(request,context):
    if request.method =="POST":
        motor_PN_search = request.POST.get('motor_PN_search')
        motor_model_search = request.POST.get('motor_model_search')
        motor_code_search = request.POST.get('motor_code_search')
        # print(motor_PN_search,motor_model_search,motor_code_search)
        motorinfoobj_list = models.MotorInfo.objects.filter(motor_PN__icontains = motor_PN_search,motor_model__icontains = motor_model_search,motor_code__icontains = motor_code_search).all()
        context['motorinfoobj_list'] = motorinfoobj_list
    return render(request,'test_app/search.html',context)