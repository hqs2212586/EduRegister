# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from rest_framework import serializers
from . import models


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:    # 配置元信息
        model = models.School      # 课程分类表
        fields = "__all__"


class AcademySerializer(serializers.ModelSerializer):
    # SerializerMethodField使用，获取显示外联字段
    school_info = serializers.SerializerMethodField(read_only=True)

    def get_school_info(self, obj):
        school_obj = obj.school   # 正向查询
        return {"id": school_obj.id}

    class Meta:
        model = models.Academy
        fields = "__all__"


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Major
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="get_gender_display")   # 中文展示

    class Meta:
        model = models.Student
        fields = "__all__"
