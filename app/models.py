from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class UserInfo(models.Model):
    # '''用户表'''
    UserName = models.CharField(max_length=128, unique=True)
    pwd = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=9, default=0, decimal_places=2)
    current_cycle_start = models.DateTimeField(default=timezone.now)
    tokens_used_in_current_cycle = models.IntegerField(default=0)
    total_tokens_used = models.IntegerField(default=0)

    def __str__(self):
        return self.UserName

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class UserRequest(models.Model):
    # 用户请求、响应表
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    tokens_used = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    Req_status = models.CharField(max_length=32)


class UserOrder(models.Model):
    # '''用户订单表'''
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=32)
    Ord_status = models.CharField(max_length=32)
