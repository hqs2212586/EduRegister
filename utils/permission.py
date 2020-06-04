# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# from rest_framework.permissions import BasePermission   # 权限管理基类
# from accounts.models import Account
#
#
# class SiteAdminPermission(BasePermission):
#     message = "您没有该权限，请向管理员申请！"
#
#     def has_permission(self, request, view):
#         username = request.user    # 获取前面认证过的信息
#         user_type = Account.objects.filter(name=username).first().user_type
#         if user_type == 2 or user_type == 3:
#             # 通过权限认证
#             return True
#         else:
#             # 未通过权限认证
#             return False
#
#
# class SchoolAdminPermission(BasePermission):
#     message = "只有管理员才能访问！"
#
#     def has_permission(self, request, view):
#         username = request.user    # 获取前面认证过的信息
#         user_type = Account.objects.filter(name=username).first().user_type
#         if user_type == 3:
#             # 通过权限认证
#             return True
#         else:
#             # 未通过权限认证
#             return False
