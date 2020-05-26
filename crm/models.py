# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from django.db import models
from django.contrib.contenttypes.models import ContentType
from accounts.models import Account


__all__ = ["School", "Academy", "Major", "Student", "UserInfo"]


"""
null=True：数据库创建时该字段可不填，用NULL填充
blank=True：创建数据库记录时该字段可传空白
unique=True：这个数据字段的值在整张表中必须是唯一的
"""

class School(models.Model):
    """学校表"""
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="院校", max_length=32, unique=True, help_text="必填")
    logo = models.ImageField(upload_to="school/%Y-%m",
                             verbose_name="学校LOGO", help_text="必填")    # 上传图片路径，以年月划分文件夹
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = "学校表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Site(models.Model):
    """站点表"""
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="站点名称", max_length=32, help_text="必填")
    schools = models.ForeignKey(to=School, to_field="nid", on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = "站点表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Academy(models.Model):
    """院系表"""
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="院系名称", max_length=32, help_text="必填")
    # 与学校建立一对多关系，外键字段建立在多的一方
    # to_field:指定当前关系与被关联对象中的哪个字段关联
    site = models.ForeignKey(to=Site, to_field="nid", on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = "院系表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Major(models.Model):
    """专业表"""
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="专业名称", max_length=32, help_text="必填")
    # 专业与学院建立多对一关系
    academies = models.ForeignKey(verbose_name="院系", to="Academy", to_field="nid", on_delete=None)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        unique_together = ('title', 'academies')   # 专业与学院联合唯一
        verbose_name = "专业表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Student(models.Model):
    """学生表"""
    nid = models.AutoField(primary_key=True)
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
    postcode = models.CharField(verbose_name='邮编', max_length=6, blank=True, null=True, help_text='选填')
    tel = models.CharField(verbose_name='联系电话1', max_length=11, help_text='必填')
    tel_2 = models.CharField(verbose_name='联系电话2', max_length=11, help_text='选填', null=True, blank=True)
    # 报读专业
    majors = models.ManyToManyField(verbose_name='报读专业', to='Major', help_text="必填")
    # auto_now_add：创建时间不用复制，默认使用当前时间赋值
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    # 学生状态
    status_choices = (
        (0, "未审核"),
        (1, "审核通过"),
        (2, "审核拒绝")
    )
    student_status = models.IntegerField(choices=status_choices, default=0)
    # 招生老师
    users = models.ForeignKey(verbose_name="验证码", to="UserInfo", to_field='nid',
                                   on_delete=models.CASCADE, help_text='必填')
    # 备注
    memo = models.CharField(verbose_name="备注", blank=True, null=True, max_length=128, help_text="选填")

    class Meta:
        verbose_name = "学生表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    """
    员工表
    """
    nid = models.AutoField(primary_key=True)
    code = models.CharField(verbose_name="验证码", max_length=16, help_text='必填')
    title = models.CharField(verbose_name="员工姓名", max_length=16, help_text='必填')
    tel = models.CharField(verbose_name="手机号", max_length=11, help_text='必填')
    email = models.EmailField(verbose_name="邮箱", max_length=32, blank=True,
                              null=True, help_text='选填')
    gender_choices = (
        (0, "男"),
        (1, "女")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, help_text="必填")
    identity_num = models.CharField(verbose_name='身份证号', max_length=18, help_text='必填')
    avatar = models.ImageField(upload_to="user/%user/%Y-%m", verbose_name='用户头像')
    # 模仿 SQL 约束 ON DELETE CASCADE 的行为，换句话说，删除一个对象时也会删除与它相关联的外键对象
    academies = models.ForeignKey(verbose_name="院系", to="Academy", to_field="nid", on_delete=None)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    # 员工表Userinfo与rbac.User表做一对一关联
    user = models.OneToOneField(to=Account, to_field="nid", null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "用户详情表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%s)" % (self.title, self.code)    # 名称和验证码

