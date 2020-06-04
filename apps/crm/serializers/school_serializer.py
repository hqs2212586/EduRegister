# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework import serializers
from ..models import SchoolInfo


class SchoolInfoSerializer(serializers.ModelSerializer):
    """学校信息序列化"""

    class Meta:
        model = SchoolInfo
        fields = '__all__'


class SchoolListSerializer(serializers.ModelSerializer):
    """学校列表序列化"""

    class Meta:
        model = SchoolInfo
        fields = '__all__'
