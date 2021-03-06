# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from utils.custom import CommonPagination, RbacPermission
from ..serializers.student_serializer import StudentInfoSerializer, StudentListSerializer
from ..models import StudentInfo


class StudentInfoViewSet(ModelViewSet):
    """学生字典管理：增删改查"""
    perms_map = (
        {'*': 'admin'}, {'*': 'enrollstu_all'}, {'get': 'enrollstu_list'}, {'post': 'enrollstu_create'},
        {'put': 'enrollstu_edit'}, {'delete': 'enrollstu_delete'})
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('name',)
    search_fields = ('name',)
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (RbacPermission,)


class StudentListView(ListAPIView):
    """学生列表视图"""
    queryset = StudentInfo.objects.all()
    serializer_class = StudentListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('name',)
    ordering_fields = ('id', )
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)