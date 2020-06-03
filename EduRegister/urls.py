"""EduRegister URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url, include
from django.views.static import serve
from EduRegister import settings
from rest_framework.documentation import include_docs_urls    # 自动接口文档路由对应视图


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include("crm.urls")),
    path(r'', include("rbac.urls")),

    # 总路由中添加接口文档路径
    path('docs/', include_docs_urls()),

    # media路径配置
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
]