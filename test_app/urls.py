# -*- coding: utf-8 -*-
# @Author: Sylvain-Yu
# @Date:   2019-07-12 17:13:07
# @Last Modified by:   Sylvain-Yu
# @Last Modified time: 2019-07-17 14:27:31
from django.urls import path
from . import views
app_name ='test_app'

urlpatterns = [
    path('', views.main, name='dataview'),
    path('highspeed/',views.highspeed, name ='highspeed'),
    path('basic/',views.basic,name = 'basic'),
    path('search/',views.search,name = 'search'),
    path('motor_logout/',views.motor_logout,name ='motor_logout'),
    path('index/',views.index,name='index'),
]
