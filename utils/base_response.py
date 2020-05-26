# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

# 自定义统一封装Response


class BaseResponse(object):
    def __init__(self):
        self.code = 1000     # 默认码
        self.data = {}
        self.error = None    # 错误信息

    @property       # 方法变属性
    def dict(self):
        print('dict信息', self.__dict__)
        return self.__dict__

