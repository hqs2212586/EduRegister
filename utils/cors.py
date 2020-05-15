# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'


from django.middleware.common import CommonMiddleware   # 通过它找到要引入的模块
from django.utils.deprecation import MiddlewareMixin


class CORSMiddleware(MiddlewareMixin):
    """自定义中间件"""
    def process_response(self, request, response):
        # 添加响应头
        # 允许您的域名来获取数据
        response["Access-Control-Allow-Origin"] = "*"
        # 允许你携带Content-Type请求头，这里不能写*,
        # 允许跨域设置中需要让 authorization 通过
        response["Access-Control-Allow-Headers"] = "Content-Type, x-requested-with ,Authorization"
        # 允许你发送GET/POST/DELETE/PUT
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        return response


