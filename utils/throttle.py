# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import time
from rest_framework.throttling import BaseThrottle


VISIT_RECORD = {}    # 访问列表: {ip: [time1, time2, ... , time5]}


class MyThrottle(BaseThrottle):
    """自定义限制类"""
    def __init__(self):
        self.history = None

    def allow_request(self, request, view):
        """实现限流逻辑"""
        # 以ip限流：要求访问站点的频率一分钟不超过5次
        # 1、获取请求的ip地址
        remote_ip = request.META.get("REMOTE_ADDR")
        c_time = time.time()

        # 2、判断ip是否在地址列表
        if remote_ip not in VISIT_RECORD:
            # 若不在，添加key,value
            VISIT_RECORD[remote_ip] = [c_time, ]
            return True
        else:
            # 若在，加入列表
            history = VISIT_RECORD.get(remote_ip)    # ip对应的历史记录

            # 确保列表最新访问和最老访问时间差是1分钟
            while history and history[0] - history[-1] > 60:
                history.pop()              # 删除最后一个
            self.history = history

            # 得到列表的长度，判断是否是允许范围
            if len(history) < 5:
                # 未达到频率限制
                history.insert(0, c_time)     # 加到第一个
                return True
            else:
                return False

    def wait(self):
        # 返回还剩多久继续访问
        c_time = 60 - (self.history[0] - self.history[-1])
        return c_time