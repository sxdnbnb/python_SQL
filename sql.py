# _*_coding : utf-8 _*_
# @Time : 2022/7/11 16:03
# @Author : SunShine
# @File : sql
# @Project : python_SQL
#!/usr/bin/env python

# -*- coding:utf- -*-

#-*- coding:utf-8 -*-
"""
配置字段说明如下：
1、mysql
常见mysql参数。

2、hive
database:数据库名
table: 状态日志的表名
table_app:app控制的日志表

"""
import pymysql
mysql= {
		'host':'localhost',
		'port':3306,
		'user':'root',
		'password':'6446530',
		'db':'db1'
		# charset='utf8'
}

db=pymysql.connect(host=mysql['host'],port=mysql['port'],user=mysql['user'],passwd=mysql['password'],db=mysql['db'])
print('连接成功')
cursor=db.cursor()#用于数据库查询结果以及执行sql语句
sql='SELECT * from user;'
cursor.execute(sql)
n=cursor.fetchall()
print(n)
db.commit()
cursor.close()
db.close()
