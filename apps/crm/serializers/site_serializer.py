# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework import serializers
from ..models import SiteInfo


class SiteInfoSerializer(serializers.ModelSerializer):
    """学校信息序列化"""

    class Meta:
        model = SiteInfo
        fields = '__all__'


class SiteListSerializer(serializers.ModelSerializer):
    """学校列表序列化"""

    class Meta:
        model = SiteInfo
        fields = '__all__'