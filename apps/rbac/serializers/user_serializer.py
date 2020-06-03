# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import re
from rest_framework import serializers
from ..models import UserProfile


class UserListSerializer(serializers.ModelSerializer):
    """用户列表的序列化"""
    roles = serializers.SerializerMethodField()

    def get_roles(self, obj):
        return obj.roles.values()

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'name', 'mobile', 'email', 'image',
                  'department', 'position', 'superior', 'is_active','roles']
        depth = 1


class UserModifySerializer(serializers.ModelSerializer):
    """用户编辑的序列化"""
    mobile = serializers.CharField(max_length=11)

    def validated_mobile(self, mobile):
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码不合法")
        return mobile

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'name', 'mobile', 'email', 'image',
                  'department', 'position', 'superior', 'is_active', 'roles']


class UserCreateSerializer(serializers.ModelSerializer):
    """创建用户序列化"""
    username = serializers.CharField(required=True, allow_blank=False)
    mobile = serializers.CharField(max_length=11)

    def validated_username(self, username):
        if UserProfile.objects.filter(username=username):
            raise serializers.ValidationError(username + "账号已存在")
        return username

    def validated_mobile(self, mobile):
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码不合法")
        if UserProfile.objects.filter(mobile=mobile):
            raise serializers.ValidationError("手机号已经被注册")
        return mobile

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'name', 'mobile', 'email', 'department',
                  'position', 'is_active', 'roles', 'password']


class UserInfoListSerializer(serializers.ModelSerializer):
    """公共users"""
    class Meta:
        model = UserProfile
        fields = ('id','name','mobile','email','position')
