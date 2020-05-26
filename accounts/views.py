import redis
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from .serializers import AccountSerializer
from utils.base_response import BaseResponse
from utils.redis_pool import POOL         # 连接池
from utils.throttle import MyThrottle     # 频率
from . import models


class RegisterView(APIView):
    versioning_class = URLPathVersioning
    throttle_classes = [MyThrottle, ]      # 局部频率

    def post(self, request, *args, **kwargs):
        res = BaseResponse()      # 实例化响应
        # 用序列化器做校验
        ser_obj = AccountSerializer(data=request.data)
        if ser_obj.is_valid():
            # 校验通过
            ser_obj.save()
            res.data = ser_obj.data
        else:
            # 校验失败
            res.data = 1020
            res.error = ser_obj.errors
        print('校验结果', res.data, res.dict)
        return Response(res.dict)


class LoginView(APIView):
    versioning_class = URLPathVersioning
    throttle_classes = [MyThrottle, ]  # 局部频率

    def post(self, request, *args, **kwargs):
        res = BaseResponse()
        name = request.data.get("name", "")
        pwd = request.data.get("password", "")
        user_obj = models.Account.objects.filter(username=name, pwd=pwd).first()

        if not user_obj:
            res.code = 1030
            res.error = "用户名或密码错误"
            print(res.dict, type(res.dict))
            return Response(res.dict)
        # 用户登录成功生成一个token写入redis
        conn = redis.Redis(connection_pool=POOL)
        try:
            token = uuid.uuid4()   # 生成随机字符串,类型是:<class 'uuid.UUID'>
            conn.set(str(token), 'user_'+ str(user_obj.nid), ex=86400)    # ex:过期时间一天
            res.data["access_token"] = token
            res.data["name"] = name
            res.data["avatar"] = 'http://127.0.0.1:8000/media/' + str(user_obj.avatar)
        except Exception as e:
            print("登录抛出的异常", e)
            res.code = 1031
            res.error = "创建令牌失败"
        print(res.dict, type(res.dict))
        return Response(res.dict)


class UserView(APIView):
    versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        """查看所有用户"""
        res = BaseResponse()
        # 这里要根据用户角色来获取


        # 通过ORM操作获取所有分类数据
        queryset = models.Account.objects.all()
        # 利用DRF序列化器去序列化数据
        ser_obj = AccountSerializer(queryset, many=True)
        # 返回
        print(request.version)
        return Response(ser_obj.data)

    def post(self, request, *args, **kwargs):
        res = BaseResponse()



