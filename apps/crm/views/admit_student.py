# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from utils.custom import CommonPagination, RbacPermission
from ..serializers.admit_student_serializer import AdmitStudentInfoSerializer, AdmitStudentListSerializer
from ..models import AdmitStudentInfo


class AdmitStudentInfoViewSet(ModelViewSet):
    """录取学生字典管理：增删改查"""
    perms_map = (
        {'*': 'admin'}, {'*': 'admitstu_all'}, {'get': 'admitstu_list'}, {'post': 'admitstu_create'},
        {'put': 'admitstu_edit'}, {'delete': 'admitstu_delete'})
    queryset = AdmitStudentInfo.objects.all()
    serializer_class = AdmitStudentInfoSerializer
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('xm',)
    search_fields = ('xm',)
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (RbacPermission,)


class AdmitStudentListView(ListAPIView):
    """录取学生列表视图"""
    queryset = AdmitStudentInfo.objects.all()
    serializer_class = AdmitStudentListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('xm',)
    ordering_fields = ('id', )
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
