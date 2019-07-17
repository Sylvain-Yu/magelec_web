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
            return redirect('login_app:login')
    return inner

def pass_user_info(f):
    @wraps(f)
    def inner(request,*arg,**kwarg):
        user_id1 = request.session.get('user_id')
        userobj = models.User.objects.filter(id = user_id1).first()
        context = {'user':userobj}
        return f(request,*arg,context)
    return inner

@check_login
@pass_user_info
def index(request,context):
    return render(request,'login_app/index.html',context)


def reindex(request):
    return redirect('login_app:login')

def login(request):
    # print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.User.objects.filter(name = username , password = password).first()
        if user:
            request.session['is_login'] = '1'
            request.session['user_id'] = user.id
            return redirect('login_app:index')
    return render(request,'login_app/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password ==password2:
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
    return redirect('login_app:login')