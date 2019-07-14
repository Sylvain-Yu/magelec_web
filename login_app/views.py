from django.shortcuts import render ,redirect
from . import models
from functools import wraps
# from django.http import Http404
# Create your views here.
def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwarg):
        if request.session.get('is_login') == '1':
            return f(request,*arg,**kwarg)
        else:
            return redirect('/account/login')
    return inner

@check_login
def index(request):
    user_id1 = request.session.get('user_id')
    userobj = models.User.objects.filter(id = user_id1).first()
    if userobj:
        return render(request,'login_app/index.html',{'user':userobj})

    return redirect('/account/login/')


def reindex(request):
    return redirect('/account/index/')

def login(request):
    # print(request.method)
    print('1')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.User.objects.filter(name = username , password = password).first()
        if user:
            request.session['is_login'] = '1'
            request.session['user_id'] = user.id
            print('run login')
            return redirect('/account/index')
    print('KK')
    return render(request,'login_app/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        sex = request.POST.get('sex')
        userobj = models.User.objects
        userobj['name'] = username
        userobj['password'] = password
        userobj['email'] = email
        userobj['sex'] = sex
        userobj.save()
    return render(request,'login_app/register.html')

def logout(request):
    request.session['is_login'] = '0'
    return redirect('/account/login/')