# -*- coding:utf-8 -*-
__author__ = 'Qiushi Huang'

import logging
import json


class ApiLoggingMiddleware(object):
    """日志记录中间件"""
    def __init__(self, get_response):
        self.get_response = get_response
        self.apiLogger = logging.getLogger('api')

    def __call__(self, request):
        try:
            body = json.loads(request.body)
        except Exception:
            body = dict()
        body.update(dict(request.POST))
        response = self.get_response(request)
        if request.method != 'GET':
            self.apiLogger.info("{} {} {} {} {} {}".format(
                request.user, request.method, request.path, body,
                response.status_code, response.reason_phrase
            ))
        return response
