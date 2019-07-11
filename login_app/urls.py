# -*- coding: utf-8 -*-
# @Author: sylvain
# @Date:   2019-07-08 14:58:03
# @Last Modified by:   sylvain
# @Last Modified time: 2019-07-09 14:05:20
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
]
