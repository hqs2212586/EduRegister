# EduRegister
基于django-restframework开发的后台系统，为注册系统提供api接口服务。

***本项目采用以下技术***

前端：

vue 2.5.17

elementUI 2.6.0

websocket

后端：

django 2.1.7

django rest framework 3.9.1

django rest framework-jwt 1.11.0

django channels 2.1.7

celery 4.2.1

软件运行环境

Python 3.7.1

MySql 5.7

操作系统：

CentOS 7

***系统更新方式***
```
cd 你的项目地址
sh upgrade.sh
更新完毕后，修改管理员密码
python manage.py changepassword admin

前端更新build后放到你的nginx静态目录
```

***基础环境安装***

1、安装npm运行环境(略)

    安装前端项目依赖包
    
    cd xops_qd/
    npm install

2、修改你的配置文件

    xops_qd/config

    dev.env.js #开发环境

    prod.env.js #生成环境

3、安装mysql依赖

```bash
# 1.安装依赖包
$ yum -y install ncurses-devel gcc-* bzip2-* bison

# 2.升级cmake工具
# 软件获取：https://cmake.org/download
$ wget https://cmake.org/files/v3.13/cmake-3.13.0-rc2.tar.gz
$ tar xf cmake-3.13.0-rc2.tar.gz   # 解压
$ ./configure     # 配置
$ make -j4        # 多核编译减少等待时间
$ make install   # 安装
# 检查是否安装完成
$ cmake --version

# 3. 升级boost库文件
# boost库获取：https://www.boost.org
# 由于这里是安装5.7的mysql,因此下载的是boost_1_59_0.tar.bz2
$ tar xf boost_1_59_0.tar.bz2    # 解压
$ mv boost_1_59_0   /usr/local/boost
```

4、安装mysql

```bash
# 4.安装mysql
# 添加用户与组
$ useradd -s /sbin/nologin -r mysql
$ mkdir -pv /usr/local/mysql/data

# 软件获取：https://www.oracle.com=>下载=>myql=>社区版本，此处下载mysql-5.7.24.tar.gz
# wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz

$ tar xf mysql-5.7.24.tar.gz      # mysql解压

# 用cmake配置
# 如果配置失败要重新配置，删除CMakeCache.txt文件即可
$ cmake . \
    -DCMAKE_INSTALL_PREFIX=/usr/local/mysql  \
    -DMYSQL_DATADIR=/usr/local/mysql/data/ \
    -DMYSQL_UNIX_ADDR=/usr/local/mysql/mysql.sock \
    -DWITH_INNBASE_STORAGE_EGNINE=1 \
    -DWITH_MYISAM_STORAGE_ENGINE=1 \
    -DENABLED_LOCAL_INFILE=1 \
    -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf-8 -DDEFAULT_COLLATION=utf8_general_ci \
    -DWITH_DEBUG=0 \
    -DWITH_EMBEDDED_SERVER=1 \
    -DDOWNLOAD_BOOST=1 -DENABLE_DOWNLOADS=1 -DWITH_BOOST=/usr/local/boost

# 解释
$ cmake . \
    -DCMAKE_INSTALL_PREFIX=/usr/local/mysql  \   # 指定安装路径
    -DMYSQL_DATADIR=/usr/local/mysql/data/ \    # 指定数据目录
    -DMYSQL_UNIX_ADDR=/usr/local/mysql/mysql.sock \   # 指定sock文件路径
    -DWITH_INNBASE_STORAGE_EGNINE=1 \    # 安装Innodb存储引擎
    -DWITH_MYISAM_STORAGE_ENGINE=1 \      # 安装myisam存储引擎
    -DENABLED_LOCAL_INFILE=1 \    # 运行使用Load data命令从本地导入数据
    -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf-8 -DDEFAULT_COLLATION=utf8_general_ci \   # 安装所有字符集、默认字符集utf-8、检验字符
    -DWITH_DEBUG=0 \    # 关闭debug
    -DWITH_EMBEDDED_SERVER=1   \   # 生成一个libmysqld.a(.so)的库，这个库同时集成了mysql服务与客户端API
    -DDOWNLOAD_BOOST=1 -DENABLE_DOWNLOADS=1 -DWITH_BOOST=/usr/local/boost   # 运行boost    允许下载boost库文件

# 编译
$ make -j4
# 安装
$ make install

# 5.启动测试
$ cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysql
$ chmod 755 /etc/init.d/mysql   # 赋权限
$ useradd -s /sbin/nologin -r mysql    # 添加用户
$ chown mysql:mysql /usr/local/mysql/ -R   # 修改目录权属
# 建立链接
$ ln -sf /usr/local/mysql/bin/*  /usr/bin/
$ ln -sf /usr/local/mysql/lib/*  /usr/lib/
$ ln -sf /usr/local/mysql/libexec/*  /usr/local/libexec
$ ln -sf /usr/local/mysql/share/man/man1/*  /usr/share/man/man1
$ ln -sf /usr/local/mysql/share/man/man8/*  /usr/share/man/man8

# 修改配置文件 /etc/my.cnf
[mysqld]
basedir=/usr/local/mysql          # mysql软件在哪
datadir=/usr/local/mysql/data   # mysql的数据在哪
socket=/usr/local/mysql/mysql.sock
symbolic-links=0
[mysqld_safe]
log-error=/var/log/mysql.log
pid-file=/var/run/mysql.pid

# 初始化数据库
$ /usr/local/mysql/bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql/ --datadir=/usr/local/mysqld/data/
# 注意：初始化后会得到一个临时密码

# 启动数据库
$ /etc/init.d/mysql start
$ lsof -i :3306  # 查看端口情况

# 修改密码
$ mysql_secure_installation   # 要使用刚刚得到的临时密码
$ mysql -uroot -pxxxxxx
# 登录数据库

```

5、安装redis（略）

6、创建python虚拟环境

```bash
# 下载python包
$ wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz

# python安装
$ tar xf python-3.7.1.tar.xz
$ cd Python-3.7.1
$ yum -y install gcc-* openssl-* libffi-devel sqlite-devel
$ ./configure --prefix=/usr/local/python3
--enable-optimizations --with-openssl=/usr/bin/oponssl # --enable-optimizations是包优化参数 
$ make -j4 # 由于有加配置优化，这个步骤会很久 
$ make install
# 建立软链
$ ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```

- 安装  
yum install git gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel libffi-devel -y  

- 多版本管理工具
1. 安装Pyenv 

```
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash  

echo 'export PATH="/$HOME/.pyenv/bin:$PATH"'>> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile 
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile 
pyenv install 3.6.8 -v
pyenv virtualenv 3.6.8 rest_xops
cd 你的项目路径
pyenv local rest_xops
```


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
   

