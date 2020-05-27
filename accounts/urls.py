# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RegisterView, LoginView, AccountListView, AccountDetailView


urlpatterns = [
    url(r'^register/$', RegisterView.as_view()),         # 注册
    url(r'^login/$', LoginView.as_view()),               # 登录
    url(r'^accounts/$', AccountListView.as_view()),                     # 账户列表
    url(r'^accounts/(?P<pk>[0-9]+)/$', AccountDetailView.as_view()),    # 账户详情
]

urlpatterns = format_suffix_patterns(urlpatterns)