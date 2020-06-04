# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework import serializers
from ..models import StudentInfo


class StudentInfoSerializer(serializers.ModelSerializer):
    """学校信息序列化"""

    class Meta:
        model = StudentInfo
        fields = '__all__'


class StudentListSerializer(serializers.ModelSerializer):
    """学校列表序列化"""

    class Meta:
        model = StudentInfo
        fields = '__all__'