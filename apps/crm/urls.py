# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from django.urls import path,include
from crm.views import school, site, train_type, grade, student
from rest_framework import routers


router = routers.SimpleRouter()
# register() 方法有两个强制参数：prefix：用于此组路由的URL前缀；viewset：处理请求的viewset类
router.register(r"schools", school.SchoolInfoViewSet, base_name="schools")
router.register(r"sites", site.SiteInfoViewSet, base_name="sites")
router.register(r"train_types", train_type.TrainTypeInfoViewSet, base_name="train_types")
router.register(r"grades", grade.GradeInfoViewSet, base_name="grades")
router.register(r"students", student.StudentInfoViewSet, base_name="students")

urlpatterns = [
    path(r'api/crm/', include(router.urls)),
    path(r'api/crm/schools/list/', school.SchoolListView.as_view(), name="school_list"),
    path(r'api/crm/sites/list/', site.SiteListView.as_view(), name="site_list"),
    path(r'api/crm/train_types/list/', train_type.TrainTypeListView.as_view(), name="traintype_list"),
    path(r'api/crm/grades/list/', grade.GradeListView.as_view(), name="grade_list"),
    path(r'api/crm/students/list/', student.StudentListView.as_view(), name="student_list")
]

