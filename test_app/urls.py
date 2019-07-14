# -*- coding: utf-8 -*-
# @Author: Sylvain-Yu
# @Date:   2019-07-12 17:13:07
# @Last Modified by:   Sylvain-Yu
# @Last Modified time: 2019-07-12 17:14:11
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='dataview'),
]
