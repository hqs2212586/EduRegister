# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


import hashlib
from rest_framework import serializers
from . import models       # 权限管理的账户表


class AccountSerializer(serializers.ModelSerializer):
    """用户序列化器"""
    def create(self, validated_data):
        # 重写pwd，用md5加盐
        pwd = validated_data["pwd"]
        pwd_salt = "hqs_password" + pwd
        md5_str = hashlib.md5(pwd_salt.encode()).hexdigest()   # hexdigest方法拿到md5的str
        user_obj = models.Account.objects.create(name=validated_data['username'], pwd=md5_str)
        return user_obj

    class Meta:
        model = models.Account      # 用户表
        fields = "__all__"

