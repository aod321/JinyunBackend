from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser



# Create your models here.

class MyUser(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sex = models.CharField(max_length=10, default='female', blank=True, verbose_name="性别")
    birthday =  models.DateTimeField(
        null=True, blank=True, default=None, verbose_name="出生日期"
    )
    rule = models.CharField(max_length=10,default="shape",blank=True, verbose_name="规则")
       
    # New fields
    subject_id = models.CharField(max_length=50, default=-1, unique=False, verbose_name="被试ID")
    name = models.CharField(max_length=100, blank=True, verbose_name="姓名")
    has_played_ipad = models.BooleanField(default=False, verbose_name="是否玩过iPad")

    # playinfo = models.ForeignKey(PlayInfo, on_delete=models.CASCADE)
    class Meta:
        db_table = 'user'



class PlayInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="infos")
    log = models.TextField(blank=True, null=True, verbose_name="实验记录")
    class Meta:
        db_table = 'playinfo'