# EduRegister
基于django-restframework开发的后台系统，为注册系统提供api接口服务。

2、安装项目运行模块
```
pip install -r requirements.txt
```
3、修改配置
```
vi rest_xops/settings.py 
# 修改数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rest_xops',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': '3306',
        'OPTIONS': { 'init_command': 'SET storage_engine=INNODB;' }
    }
}
# 修改redis
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

#修改redis
vi rest_xops/celery.py

BROKER_URL = 'redis://localhost:6379/1' # Broker配置，使用Redis作为消息中间件

CELERY_RESULT_BACKEND = 'redis://localhost:6379/1' # Backend设置，使用redis作为后端结果存储


```


4、登陆MYSQL，创建数据库

```
CREATE DATABASE eduRegister DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

5、执行创建表信息

```
python3 manage.py makemigrations rbac

python3 manage.py makemigrations crm

python3 manage.py migrate
```

**导入初始化数据**

python3 manage.py loaddata init_data/*.json

如果遇到mysql模块的问题

ImportError: libmysqlclient.so.18: cannot open shared object file: No such file or directory

则：

ln -s /usr/local/mysql/lib/libmysqlclient.so.18 /usr/lib64/libmysqlclient.so.18



6、修改管理员密码（必须操作）
    
    python3 manage.py changepassword admin
   

