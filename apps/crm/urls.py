# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    url(r'^schools/$', SchoolListView.as_view()),
    url(r'^schools/(?P<pk>[0-9]+)/$', SchoolDetailView.as_view()),
    url(r'^sites/$', SiteListView.as_view()),
    url(r'^sites/(?P<pk>[0-9]+)/$', SiteDetailView.as_view()),
    url(r'^academies/$', AcademyView.as_view()),
    url(r'^academies/(?P<pk>[0-9]+)/$', AcademyDetailView.as_view()),
    url(r'^major/$', MajorView.as_view()),
    url(r'^students/$', StudentsView.as_view()),
    url(r'^student/(?P<pk>\d+)/$', StudentView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)