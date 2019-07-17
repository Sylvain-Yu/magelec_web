# -*- coding: utf-8 -*-
# @Author: sylvain
# @Date:   2019-07-08 14:58:03
# @Last Modified by:   Sylvain-Yu
# @Last Modified time: 2019-07-17 11:07:08
from django.urls import path
from . import views

app_name = 'login_app'
#start with "accounts/"
urlpatterns = [
    path('', views.reindex, name='reindex'),
    path('index/',views.index, name = 'index'),
    path('login/',views.login, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('logout/',views.logout, name = 'logout'),
]
