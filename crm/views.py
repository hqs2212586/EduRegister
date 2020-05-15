import redis
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning   # 在url上携带版本信息
from utils.base_response import BaseResponse
from utils.my_auth import LoginAuth
from utils.permission import AdminPermission, SeniorAgentPermission
from utils.redis_pool import POOL
from .serializers import *
from . import models


CONN = redis.Redis(connection_pool=POOL)    # redis连接


class SchoolView(APIView):
    """学校"""
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get(self, request, *args, **kwargs):
        # 通过ORM操作获取所有分类数据
        queryset = models.School.objects.all()
        # 利用DRF序列化器去序列化数据
        ser_obj = SchoolSerializer(queryset, many=True)
        # 返回
        print(request.version)
        return Response(ser_obj.data)

    def post(self, request, *args, **kwargs):
        """添加学校"""
        print(request.data)
        ser_obj = SchoolSerializer(data=request.data)      # 序列化器校验前端传回的数据
        if ser_obj.is_valid():
            ser_obj.save()         # 验证成功后保存数据库
            return Response(ser_obj.validated_data)        # 返回验证通过的数据
        else:
            return Response(ser_obj.errors)                # 返回错误信息

    def put(self, request, id):
        """更新学校"""
        school_obj = models.School.objects.filter(id=id).first()
        ser_obj = SchoolSerializer(
            school_obj,           # 待更新对象
            data=request.data,    # 待更新数据
            partial=True          # 重点：进行部分验证和更新
        )
        if ser_obj.is_valid():
            ser_obj.save()        # 保存
            return Response(ser_obj.validated_data)      # 返回验证通过的数据
        else:
            return Response(ser_obj.errors)              # 返回验证错误的数据

    def delete(self, request, id):
        """删除学校"""


class AcademyView(APIView):
    """站点"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get(self, request, *args, **kwargs):
        school_id = request.query_params.get("school", 0)    # 所有学校所有院系
        # 以学校为条件获取院系
        if school_id == 0:
            queryset = models.Academy.objects.all().order_by("nid")
        else:
            # 按学校过滤
            queryset = models.Academy.objects.filter(school_id=school_id).all().order_by("nid")
        # 序列化院系数据
        ser_obj = AcademySerializer(queryset, many=True)
        return Response(ser_obj.data)


class MajorView(APIView):
    """专业"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get(self, request, *args, **kwargs):
        school_id = request.query_params.get("school", 0)  # 所有学校所有专业
        # 以学校为条件获取专业
        if school_id == 0:
            queryset = models.Major.objects.all().order_by("nid")
        else:
            # 按学校过滤
            queryset = models.Major.objects.filter(school_id=school_id).all().order_by("nid")
        # 序列化专业数据
        ser_obj = MajorSerializer(queryset, many=True)
        return Response(ser_obj.data)


class StudentsView(APIView):
    """所有学生"""
    versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        school_id = request.query_params.get("school", 0)
        # 以学校为条件获取学生
        if school_id == 0:
            queryset = models.Student.objects.all().order_by("nid")
        else:
            # 按学校过滤
            queryset = models.Student.objects.filter(school_id=school_id).all().order_by("nid")
        # 序列化学生数据
        ser_obj = StudentSerializer(queryset, many=True)
        return Response(ser_obj.data)


class StudentView(APIView):
    """单个学生"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get(self, request, *args, **kwargs):
        school_id = request.query_params.get("school", 0)
        # 以学校为条件获取学生
        if school_id == 0:
            queryset = models.Student.objects.all().order_by("nid")
        else:
            # 按学校过滤
            queryset = models.Student.objects.filter(school_id=school_id).all().order_by("nid")
        # 序列化学生数据
        ser_obj = StudentSerializer(queryset, many=True)
        return Response(ser_obj.data)

    def post(self, request, *args, **kwargs):
        res = BaseResponse()
        # 1.获取前端数据及user_id
        stu_obj = request.data.get("student_info", "")
        user_id = request.user.id

        # 2.校验数据的合法性
        # 2.1 校验课程id合法性













