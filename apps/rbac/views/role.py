# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework.viewsets import ModelViewSet
from ..models import Role
from ..serializers.role_serializer import RoleListSerializer, RoleModifySerializer
from common.custom import SearchFilter, OrderingFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class RoleViewSet(ModelViewSet):
    pass


