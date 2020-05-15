# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


from django.conf.urls import url, include
from .views import RegisterView, LoginView, UserView


urlpatterns = [
    url(r'^register/$', RegisterView.as_view()),    # 注册
    url(r'^login/$', LoginView.as_view()),          # 登录
    url(r'^account/$', UserView.as_view())          # 用户
]