# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

from django.urls import path, include
from rbac.views import user, organization, menu, role, permission
from crm.views import dict
from rest_framework import routers      # 自动URL路由到Django

router = routers.SimpleRouter()
# register() 方法的两个强制参数：(1)用于此组路由的URL前缀；(2)处理请求的viewset类。
# 附加参数base_name - 用于创建的URL名称的基本名称
router.register(r'users', user.UserViewSet, base_name="users")
router.register(r'organizations', organization.OrganizationViewSet, base_name="organization")
router.register(r'menus', menu.MenuViewSet, base_name="menus")
router.register(r'permissions', permission.PermissionViewSet, base_name="permissions")
router.register(r'roles', role.RoleViewSet, base_name="roles")
router.register(r'dicts', dict.DictViewSet, base_name="dicts")

urlpatterns = [
    path(r'api', include(router.urls)),
    path(r'auth/login/', user.UserAuthView.as_view()),
    path(r'auth/info/', user.UserInfoView.as_view(), name="user_info"),
    path(r'auth/build/menus/', organization.OrganizationTreeView.as_view(), name="build_menus"),
    path(r'api/organization/tree/', organization.OrganizationUserTreeView.as_view(), name="organization_user_tree"),
    path(r'api/menu/tree', menu.MenuTreeView.as_view(), name="menus_tree"),
    path(r'api/permission/tree/', permission.PermissionTreeView.as_view(), name="permissions_tree"),
    path(r'api/user/list/', user.UserListView.as_view(), name="user_list")
]
