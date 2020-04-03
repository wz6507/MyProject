from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from .models import *
import random
from email.mime.image import MIMEImage
from django.core.mail import EmailMessage
from rest_framework.views import APIView,Response
from primary import settings
import xlwt
import os
import datetime

class Create_XLS(object):
    """
        创建xls文件
    """
    def __init__(self):
        self.excel = xlwt.Workbook(encoding = 'utf-8')
        self.sheet = self.excel.add_sheet('用户信息')


    def write_value(self, cell, value):
        self.sheet.write(*cell, value)
        self.excel.save('static/table.xls')


    def write_values(self, cells, values):
        for i in range(len(values)):
            self.write_value(cells[i], values[i])


class Add_User_Information(APIView):
    def post(self,request):
        """
            将获取到的数据添加入数据库
            name         获取传递姓名
            age          获取传递年龄
            animal_heat  获取传递体温
            location     获取传递地理位置
        """
        name = request.data['name']
        age = request.data['age']
        animal_heat = request.data['animal_heat']
        location = request.data['location']
        if not all([name,age,animal_heat,location]):
            return Response({
                'code': 4004,
                'message' : '数据错误'
            })
        else:
            user = User()
            user.name = name
            user.age = age
            user.animal_heat = animal_heat
            user.location = location
            user.save()
            return Response({
                'code': 200,
                'message' : '成功'
            })


class Send_XLS_File(APIView):
    def get(self,request):
        """
            将xls文件以附件方式发送至邮箱
        """
        EW = Create_XLS()
        cells1 = []
        user = User.objects.filter(add_date=datetime.datetime.now().date()).all()
        values1 = ['姓名','年龄','体温','地址']
        num = 0
        for i in user:
            values1.append(i.name)
            values1.append(i.age)
            values1.append(i.animal_heat)
            values1.append(i.location)
            num += 1
        for i in range(num+1):
            for j in range(4):
                cells1.append((i, j))
        EW.write_values(cells1, values1)
        subject = '人员表格'
        email = EmailMessage(
            subject=subject,
            body='附件表格',
            from_email='1574928684@qq.com',
            to=['1574928684@qq.com']
        )
        file_2 = os.path.join(settings.STATICFILES_DIRS[0], 'table.xls')
        email.attach_file(file_2, mimetype='image/png')
        email.send()
        return Response({
            'code' : 200
        })

