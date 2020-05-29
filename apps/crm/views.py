from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning   # 在url上携带版本信息
from rest_framework import status              # 描述HTTP状态码，用于代码可读性
from .serializers import *
from . import models


class SchoolListView(APIView):
    """列出所有学校或创建一个新的学校"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get(self, request, *args, **kwargs):
        # 通过ORM操作获取所有分类数据
        queryset = models.School.objects.all()
        # 利用DRF序列化器去序列化数据
        ser_obj = SchoolSerializer(queryset, many=True)
        # 返回
        print(request.version, queryset)
        return Response(ser_obj.data)

    def post(self, request, *args, **kwargs):
        """添加学校"""
        print(request.data)
        ser_obj = SchoolSerializer(data=request.data)  # 序列化器校验前端传回的数据
        if ser_obj.is_valid():
            ser_obj.save()  # 验证成功后保存数据库
            return Response(ser_obj.validated_data, status=status.HTTP_201_CREATED)  # 返回验证通过的数据
        else:
            return Response(ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)      # 返回错误信息


class SchoolDetailView(APIView):
    """查看、更新、删除一个学校"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get_object(self, pk):
        try:
            return models.School.objects.get(pk=pk)
        except models.School.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_object(pk)
        ser_obj = SchoolSerializer(queryset)
        return Response(ser_obj.data)


    def put(self, request, pk,  *args, **kwargs):
        """更新学校"""
        queryset = self.get_object(pk)
        ser_obj = SchoolSerializer(
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
        """删除学校"""
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SiteListView(APIView):
    """站点列表查看、站点添加"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get(self, request, *args, **kwargs):
        # 通过ORM操作获取所有分类数据
        queryset = models.Site.objects.all()
        # 利用DRF序列化器去序列化数据
        ser_obj = SiteSerializer(queryset, many=True)
        # 返回
        print(request.version, queryset)
        return Response(ser_obj.data)

    def post(self, request, *args, **kwargs):
        """添加学校"""
        print(request.data)
        ser_obj = SiteSerializer(data=request.data)  # 序列化器校验前端传回的数据
        if ser_obj.is_valid():
            ser_obj.save()  # 验证成功后保存数据库
            return Response(ser_obj.validated_data, status=status.HTTP_201_CREATED)  # 返回验证通过的数据
        else:
            return Response(ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)  # 返回错误信息


class SiteDetailView(APIView):
    """查看、更新、删除一个站点"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get_object(self, pk):
        try:
            return models.Site.objects.get(pk=pk)
        except models.Site.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_object(pk)
        ser_obj = SiteSerializer(queryset)
        return Response(ser_obj.data)

    def put(self, request, pk, *args, **kwargs):
        """更新学校"""
        queryset = self.get_object(pk)
        ser_obj = SiteSerializer(
            queryset,  # 待更新对象
            data=request.data,  # 待更新数据
            partial=True  # 进行部分验证和更新
        )
        if ser_obj.is_valid():
            ser_obj.save()  # 保存
            return Response(ser_obj.validated_data)  # 返回验证通过的数据
        else:
            return Response(ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)  # 返回验证错误的数据

    def delete(self, request, pk, *args, **kwargs):
        """删除学校"""
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AcademyView(APIView):
    """学院/部门"""
    versioning_class = URLPathVersioning
    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get(self, request, *args, **kwargs):
        # 通过ORM操作获取所有分类数据
        queryset = models.Academy.objects.all()
        # 利用DRF序列化器去序列化数据
        ser_obj = AcademySerializer(queryset, many=True)
        # 返回
        print(request.version, queryset)
        return Response(ser_obj.data)

    def post(self, request, *args, **kwargs):
        """添加学院/部门"""
        print(request.data)
        ser_obj = SiteSerializer(data=request.data)  # 序列化器校验前端传回的数据
        if ser_obj.is_valid():
            ser_obj.save()  # 验证成功后保存数据库
            return Response(ser_obj.validated_data, status=status.HTTP_201_CREATED)  # 返回验证通过的数据
        else:
            return Response(ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)  # 返回错误信息


class AcademyDetailView(APIView):
    """查看、更新、删除一个站点"""
    versioning_class = URLPathVersioning

    # authentication_classes = [LoginAuth, ]
    # permission_classes = [SeniorAgentPermission, AdminPermission, ]

    def get_object(self, pk):
        try:
            return models.Academy.objects.get(pk=pk)
        except models.Academy.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_object(pk)
        ser_obj = AcademySerializer(queryset)
        return Response(ser_obj.data)

    def put(self, request, pk, *args, **kwargs):
        """更新学校"""
        queryset = self.get_object(pk)
        ser_obj = AcademySerializer(
            queryset,  # 待更新对象
            data=request.data,  # 待更新数据
            partial=True  # 进行部分验证和更新
        )
        if ser_obj.is_valid():
            ser_obj.save()  # 保存
            return Response(ser_obj.validated_data)  # 返回验证通过的数据
        else:
            return Response(ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)  # 返回验证错误的数据

    def delete(self, request, pk, *args, **kwargs):
        """删除学校"""
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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
        # 1.获取前端数据及user_id
        stu_obj = request.data.get("student_info", "")
        user_id = request.user.id

        # 2.校验数据的合法性
        # 2.1 校验课程id合法性













