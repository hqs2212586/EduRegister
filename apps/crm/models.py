# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from datetime import datetime
from django.db import models
from rbac.models import Organization


__all__ = ["SchoolInfo", "SiteInfo", "TrainTypeInfo", "GradeInfo", "StudentInfo"]


"""
null=True：数据库创建时该字段可不填，用NULL填充
blank=True：创建数据库记录时该字段可传空白
unique=True：这个数据字段的值在整张表中必须是唯一的
"""

class TimeAbstract(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True


class SchoolInfo(TimeAbstract):
    """学校表"""
    title = models.CharField(verbose_name="院校", max_length=32, unique=True, help_text="必填")
    logo = models.ImageField(verbose_name="LOGO",upload_to="school/%title", default="school/default_logo.png", help_text="必填")
    organization = models.ForeignKey(to=Organization, to_field="id", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "学校表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class SiteInfo(TimeAbstract):
    """站点表"""
    title = models.CharField(verbose_name="站点名称", max_length=32, help_text="必填", unique=True)
    schools = models.ForeignKey(to=SchoolInfo, to_field="id", on_delete=models.CASCADE)
    organization = models.ForeignKey(to=Organization, to_field="id", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "站点表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class TrainTypeInfo(TimeAbstract):
    """培养类型表"""
    title = models.CharField(verbose_name="培养类型", max_length=32, help_text="必填", unique=True)

    class Meta:
        verbose_name = "培养类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GradeInfo(TimeAbstract):
    """年级/招生批次"""
    title = models.CharField(verbose_name="年级名称", max_length=255, help_text="必填", unique=True)
    status_choices = (
        (0, "之前学年"),
        (1, "当前学年"),
        (2, "未来学年")
    )
    schools = models.ForeignKey(to=SchoolInfo, to_field="title", on_delete=models.CASCADE)
    begin_time = models.DateTimeField(verbose_name="开始时间", blank=True, null=True, default=None)
    end_time = models.DateTimeField(verbose_name="结束时间", blank=True, null=True, default=None)
    status = models.SmallIntegerField(verbose_name="学年状态", choices=status_choices, help_text="必填")

    class Meta:
        verbose_name = "入学学年表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class StudentInfo(TimeAbstract):
    """学生表"""
    name = models.CharField(verbose_name="姓名", max_length=48)
    gender_choices = (
        (0, "男"),
        (1, "女")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, help_text="必填")
    nation = models.CharField(verbose_name='民族', max_length=32, default='汉族', help_text='必填')
    birth_place = models.CharField(verbose_name='籍贯', max_length=64, default='身份证上:xx省xx市', help_text='必填')
    identity_num = models.CharField(verbose_name='身份证号', max_length=18, help_text='必填')
    address = models.CharField(verbose_name='常用住址', max_length=128, help_text='必填')
    tel = models.CharField(verbose_name='手机号', max_length=11, help_text='必填')
    # 报读专业
    majors = models.CharField(verbose_name='报读专业', max_length=64, help_text="必填")
    # 学生状态
    status_choices = (
        (0, "未审核"),
        (1, "审核通过"),
        (2, "审核拒绝")
    )
    student_status = models.IntegerField(choices=status_choices, default=0, verbose_name="学生状态")
    grades = models.ForeignKey(verbose_name="入学学年", to=GradeInfo, to_field="title", on_delete=models.CASCADE)
    sites = models.ForeignKey(verbose_name="招生站点", to=SiteInfo, to_field='title',
                                   on_delete=models.CASCADE, help_text='必填')
    # 备注
    memo = models.CharField(verbose_name="备注", blank=True, null=True, max_length=128, help_text="选填")

    class Meta:
        verbose_name = "学生表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# class UserInfo(models.Model):
#     """
#     员工信息表
#     """
#     nid = models.AutoField(primary_key=True)
#     code = models.CharField(verbose_name="验证码", max_length=16, help_text='必填')
#     title = models.CharField(verbose_name="员工姓名", max_length=16, help_text='必填')
#     tel = models.CharField(verbose_name="手机号", max_length=11, help_text='必填')
#     email = models.EmailField(verbose_name="邮箱", max_length=32, blank=True,
#                               null=True, help_text='选填')
#     gender_choices = (
#         (0, "男"),
#         (1, "女")
#     )
#     gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, help_text="必填")
#     identity_num = models.CharField(verbose_name='身份证号', max_length=18, help_text='必填')
#     create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
#     update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
#     # 员工表Userinfo与rbac.User表做一对一关联
#     user = models.OneToOneField(to=Account, to_field="nid", null=True, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name = "用户详情表"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return "%s(%s)" % (self.title, self.code)    # 名称和验证码

