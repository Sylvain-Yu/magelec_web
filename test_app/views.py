from django.shortcuts import render, redirect, HttpResponse
from functools import wraps
from login_app import models as login_app_models
from . import models
from datetime import timedelta
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
            print(motorhighspeedobj_list)
            context['motorhighspeedobj_list'] = motorhighspeedobj_list
    except Exception as e:
        print(e)
    return render(request,'test_app/dataview.html',context)


@check_login
@pass_info
def motor_login(request,context):
    if request.method =='POST':
        motor_id = request.POST.get('motorindex')
        request.session['motor_id'] = motor_id
        print(motor_id)
        return redirect('test_app:index')
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
def currentvstorque(request,context):
    motorinfoobj = context['motorinfoobj']
    cvtobj = models.CurrentVsTorque()
    context['cooling_type_list'] = cvtobj.cooling_type_list
    context['forward_direction_list'] = cvtobj.forward_direction_list
    pass
    return render(request,'test_app/currentvstorque.html',context)


@pass_info
@check_login
def highspeed(request,context):
    context['forward_direction_list'] = models.HighSpeed.forward_direction_list
    motorinfoobj = context['motorinfoobj']
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
            highspeedobj.rotate_direction = request.POST.get('rotate_direction')
            highspeedobj.comment = request.POST.get('comment')
            if request.POST.get('passornot') == 'on':
                highspeedobj.passornot = True
            else:
                highspeedobj.passornot = False
            highspeedobj.motorinfo = motorinfoobj
            highspeedobj.save()
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
                motorinfo.motor_type_options_eeprom = request.POST.get('eeprom')
                motorinfo.comment = request.POST.get('comment')
                motorinfo.recorder = context['user']
                motorinfo.save()
                # 数据留存设置
                request.session['motor_id'] = motorinfo.id
                return redirect('test_app:dataview')
        except Exception as e:
            print(e)
    return render(request,'test_app/basic.html',context)


@pass_info
@check_login
def search(request,context):
    if request.method =="POST":
        motor_PN_search = request.POST.get('motor_PN_search')
        motor_model_search = request.POST.get('motor_model_search')
        motor_code_search = request.POST.get('motor_code_search')
        print(motor_PN_search,motor_model_search,motor_code_search)
        motorinfoobj_list = models.MotorInfo.objects.filter(motor_PN__contains = motor_PN_search,motor_model__contains = motor_model_search,motor_code__contains = motor_code_search).all()
        context['motorinfoobj_list'] = motorinfoobj_list
    return render(request,'test_app/search.html',context)