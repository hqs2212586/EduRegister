# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^school/$', SchoolView.as_view()),
    url(r'^academy/$', AcademyView.as_view()),
    url(r'^major/$', MajorView.as_view()),
    url(r'^students/$', StudentsView.as_view()),
    url(r'^student/(?P<pk>\d+)/$', StudentView.as_view())
]