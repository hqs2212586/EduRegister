# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework import serializers
from ..models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    """组织架构序列化"""
    type = serializers.ChoiceField(choices=Organization.organization_type_choices, default="school")

    class Meta:
        model = Organization
        fields = "__all__"


class UserSerializer(serializers.Serializer):
    """用户序列化"""
    id = serializers.IntegerField()
    label = serializers.CharField(max_length=20, source="name")


class OrganizationUserTreeSerializer(serializers.ModelSerializer):
    """组织架构树序列化"""
    # 返回关联属性的类的__str__方法的值
    label = serializers.StringRelatedField(source="name")
    children = UserSerializer(many=True, read_only=True, source="userprofile_set")

    class Meta:
        model = Organization
        fields = ('id', 'label', 'pid', 'children')