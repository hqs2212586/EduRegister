# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from utils.custom import CommonPagination, RbacPermission
from utils.base_response import BaseResponse
from utils.code import NO_CONTENT
from ..serializers.site_serializer import SiteInfoSerializer, SiteListSerializer
from ..models import SiteInfo


class SiteInfoViewSet(ModelViewSet):
    """学校字典管理：增删改查"""
    perms_map = (
        {'*': 'admin'}, {'*': 'site_all'}, {'get': 'site_list'}, {'post': 'site_create'},
        {'put': 'site_edit'}, {'delete': 'site_delete'})
    queryset = SiteInfo.objects.all()
    serializer_class = SiteInfoSerializer
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('title',)
    search_fields = ('title',)
    ordering_fields = ('id',)
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (RbacPermission,)

    # def get_serializer_class(self):
    #     # 根据请求类型动态变更serializer
    #     if self.action == 'list':
    #         return SiteInfoSerializer
    #     return SiteListSerializer

    def destroy(self, request, *args, **kwargs):
        # 删除其他关联资产的数据
        instance = self.get_object()
        id = str(kwargs['pk'])
        # projects = Project.objects.filter(
        #     Q(server_ids__icontains=id + ',') | Q(server_ids__in=id) | Q(server_ids__endswith=',' + id)).values()
        # if projects:
        #     for project in projects:
        #         server_ids = project['server_ids'].split(',')
        #         server_ids.remove(id)
        #         server_ids = ','.join(server_ids)
        #         Project.objects.filter(id=project['id']).update(server_ids=server_ids)
        self.perform_destroy(instance)

        return BaseResponse(status=NO_CONTENT)


class SiteListView(ListAPIView):
    """学校列表视图"""
    queryset = SiteInfo.objects.all()
    serializer_class = SiteListSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('title',)
    ordering_fields = ('id', )
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)