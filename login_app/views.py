from django.shortcuts import render ,redirect
from . import models
# from django.http import HttpResponse
# Create your views here.


def main(request):
    return render(request,'login_app/index.html')

def reindex(request):
    return redirect('/index/')

def index(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_list = models.User.objects.filter(name = username , password = password).first()
        if user_list:
            email = user_list.email
            sex = user_list.sex
            sex_dict = dict(models.User.gender)
            sex = sex_dict[sex]
            create_time = user_list.c_time
            context = {'name':username,
            'password':password,
            'sex':sex,
            'email':email,
            'create_time':create_time,
            }
            return render(request,'login_app/userinfo.html',context)
    return render(request,'login_app/login.html')

def register(request):
    pass
    return render(request,'login_app/register')

def logout(request):
    pass
    return redirect('/index/')