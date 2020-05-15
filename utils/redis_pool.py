# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import redis

POOL = redis.ConnectionPool(
    host="127.0.0.1",
    port=6379,
    decode_responses=True,     # 字符串格式
    max_connections=100        # 最大连接数
)