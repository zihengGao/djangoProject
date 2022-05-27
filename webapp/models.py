from django.db import models
from django.http import HttpResponse
from django.shortcuts import render

# # 创建一个数据库user表模型
class User(models.Model):
    # 如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列
    id = models.AutoField(primary_key=True)
    # 类里面的字段代表数据表中的字段(username)，数据类型则由CharField（相当于varchar）
    # username = models.CharField(max_length=100)
    # # 密码
    # password = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    age = models.CharField(max_length=50)




