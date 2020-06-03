# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from django.urls import path,include
from crm.views import school, site, train_type, grade, student
from rest_framework import routers


router = routers.SimpleRouter()
# register() 方法有两个强制参数：prefix：用于此组路由的URL前缀；viewset：处理请求的viewset类
router.register(r"schools", school.SchoolViewSet, base_name="schools")
router.register(r"sites", site.SiteViewSet, base_name="sites")
router.register(r"train_types", train_type.TrainTypeViewSet, base_name="train_types")
router.register(r"grades", grade.GradeViewSet, base_name="grades")
router.register(r"students", student.StudentViewSet, base_name="students")

urlpatterns = [
    path(r'api/', include(router.urls)),
]

