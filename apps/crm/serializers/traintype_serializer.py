# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


from rest_framework import serializers
from ..models import TrainTypeInfo


class TrainTypeInfoSerializer(serializers.ModelSerializer):
    """培养类型信息序列化"""

    class Meta:
        model = TrainTypeInfo
        fields = '__all__'


class TrainTypeListSerializer(serializers.ModelSerializer):
    """培养类型列表序列化"""

    class Meta:
        model = TrainTypeInfo
        fields = '__all__'