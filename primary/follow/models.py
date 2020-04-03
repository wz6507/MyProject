from django.db import models
import django.utils.timezone as timezone

class User(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=10,default='',verbose_name='姓名')
    age = models.IntegerField(default=0,verbose_name='年龄')
    animal_heat = models.DecimalField( max_digits=5, decimal_places=2,verbose_name='体温')
    location = models.CharField(max_length=50,default='',verbose_name='地理位置')
    add_date = models.DateField(auto_now_add=True,verbose_name='创建时间')
    class Meta:
        db_table = 'user'