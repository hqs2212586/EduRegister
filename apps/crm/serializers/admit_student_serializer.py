# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework import serializers
from ..models import AdmitStudentInfo


class AdmitStudentInfoSerializer(serializers.ModelSerializer):
    """录取学生信息序列化"""

    class Meta:
        model = AdmitStudentInfo
        fields = '__all__'


class AdmitStudentListSerializer(serializers.ModelSerializer):
    """录取学生列表序列化"""

    class Meta:
        model = AdmitStudentInfo
        fields = '__all__'
