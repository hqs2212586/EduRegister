from django.db import models

__all__ = ["Account"]


class Account(models.Model):
    """用户表"""
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, verbose_name="用户名", help_text="必填")
    pwd = models.CharField(max_length=64, verbose_name="密文密码", help_text="必填")
    avatar = models.CharField(max_length=255, verbose_name="头像", help_text="必填")    # 头像保存在前台
    # 注册用户状态
    status_choices = (
        (0, "未审核"),
        (1, "审核通过"),
        (2, "审核拒绝")
    )
    user_status = models.IntegerField(choices=status_choices, default=0)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)     # 字段的值设置为创建时的时间
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)         # 每次修改model，都会自动更新

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username