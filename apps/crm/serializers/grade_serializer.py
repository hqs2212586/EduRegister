# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework import serializers
from ..models import GradeInfo


class GradeInfoSerializer(serializers.ModelSerializer):
    """学校信息序列化"""

    class Meta:
        model = GradeInfo
        fields = '__all__'


class GradeListSerializer(serializers.ModelSerializer):
    """学校列表序列化"""

    class Meta:
        model = GradeInfo
        fields = '__all__'