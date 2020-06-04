# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


from rest_framework import serializers
from ..models import Dict

class DictSerializer(serializers.ModelSerializer):
    '''
    字典序列化
    '''
    class Meta:
        model = Dict
        fields = '__all__'


class DictTreeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField(max_length=20, source='value')
    pid = serializers.PrimaryKeyRelatedField(read_only=True)