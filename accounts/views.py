import redis
import uuid
from django.http import Http404
from rest_framework import status              # 描述HTTP状态码，用于代码可读性
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from .serializers import AccountSerializer
from utils.base_response import BaseResponse
from utils.redis_pool import POOL         # 连接池
from utils.throttle import MyThrottle     # 频率
from . import models


CONN = redis.Redis(connection_pool=POOL)       # redis连接


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
        name = request.data.get("username", "")
        pwd = request.data.get("pwd", "")     # 前端传递的密码
        user_obj = models.Account.objects.filter(username=name, pwd=pwd).first()

        if not user_obj:
            res.code = 1030
            res.error = "用户名或密码错误"
            print(res.dict, type(res.dict))
            return Response(res.dict)
        # 用户登录成功生成一个token写入redis
        try:
            token = uuid.uuid4()   # 生成随机字符串,类型是:<class 'uuid.UUID'>
            CONN.set(str(token), 'user_'+ str(user_obj.nid), ex=86400)    # ex:过期时间一天
            res.data["access_token"] = token
            res.data["name"] = name
            res.data["avatar"] = 'http://127.0.0.1:8000/media/' + str(user_obj.avatar)
        except Exception as e:
            print("登录抛出的异常", e)
            res.code = 1031
            res.error = "创建令牌失败"
        print(res.dict, type(res.dict))
        return Response(res.dict)


class AccountListView(APIView):
    """账户列表、账户添加"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get(self, request, *args, **kwargs):
        # 通过ORM操作获取所有分类数据
        queryset = models.Account.objects.all()
        # 利用DRF序列化器去序列化数据
        ser_obj = AccountSerializer(queryset, many=True)
        # 返回
        print(request.version, queryset)
        return Response(ser_obj.data)

    def post(self, request, *args, **kwargs):
        """添加学校"""
        print(request.data)
        ser_obj = AccountSerializer(data=request.data)  # 序列化器校验前端传回的数据
        if ser_obj.is_valid():
            ser_obj.save()  # 验证成功后保存数据库
            return Response(ser_obj.validated_data, status=status.HTTP_201_CREATED)  # 返回验证通过的数据
        else:
            return Response(ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)      # 返回错误信息


class AccountDetailView(APIView):
    """查看、更新、删除一个账户"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get_object(self, pk):
        try:
            return models.Account.objects.get(pk=pk)
        except models.Account.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        """查看账户"""
        queryset = self.get_object(pk)
        ser_obj = AccountSerializer(queryset)
        return Response(ser_obj.data)


    def put(self, request, pk,  *args, **kwargs):
        """更新账户"""
        queryset = self.get_object(pk)
        ser_obj = AccountSerializer(
            queryset,             # 待更新对象
            data=request.data,    # 待更新数据
            partial=True          # 进行部分验证和更新
        )
        if ser_obj.is_valid():
            ser_obj.save()        # 保存
            return Response(ser_obj.validated_data)      # 返回验证通过的数据
        else:
            return Response(ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)    # 返回验证错误的数据

    def delete(self, request, pk, *args, **kwargs):
        """删除账户"""
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
