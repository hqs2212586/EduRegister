from django.db import models
from django.contrib.auth.models import User, Group

__all__ = ["Account"]


class Account(User):
    """用户表"""
    nid = models.AutoField(primary_key=True)
    # 注册用户状态
    status_choices = (
        (0, "未审核"),
        (1, "审核通过"),
        (2, "审核拒绝")
    )
    user_status = models.IntegerField(choices=status_choices, default=0)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    type_choice = (
        (1, "普通用户"),
        (2, "高级用户"),
        (3, "部门管理员"),
        (4, "学校管理员"),
        (5, "系统管理员")
    )
    user_type = models.IntegerField(choices=type_choice, default=1)

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username