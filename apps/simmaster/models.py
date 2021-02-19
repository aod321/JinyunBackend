from django.db import models
from django.conf import settings

CARRIER_LIST = [
    (0, "未设置"),
    (1, "移动"),
    (2, "联通"),
    (3, "电信"),
    (4, "其他"),
]

PROVINCE_SETTINGS = [
    (0, "未设置"),
    (1, "北京"),
    (2, "天津"),
    (3, "河北"),
    (4, "山西"),
    (5, "内蒙古"),
    (6, "辽宁"),
    (7, "吉林"),
    (8, "黑龙江"),
    (9, "上海"),
    (10, "江苏"),
    (11, "浙江省"),
    (12, "安徽"),
    (13, "福建"),
    (14, "江西"),
    (15, "山东"),
    (16, "河南"),
    (17, "湖北"),
    (18, "湖南"),
    (19, "广东"),
    (20, "广西"),
    (21, "海南"),
    (22, "重庆"),
    (23, "四川"),
    (24, "贵州"),
    (25, "云南"),
    (26, "西藏"),
    (27, "陕西"),
    (28, "甘肃省"),
    (29, "青海"),
    (30, "宁夏"),
    (31, "新疆"),
    (32, "台湾"),
    (33, "香港特别行政区"),
    (34, "澳门"),
]

SEX_LIST = [(1, "女"), (2, "男")]


# Create your models here.
class SimList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    sim_number = models.CharField(max_length=50, verbose_name='SIM卡号', blank=True)
    carrier = models.SmallIntegerField(choices=CARRIER_LIST, verbose_name='运营商', default=0)
    location = models.SmallIntegerField(choices=PROVINCE_SETTINGS, verbose_name='归属地', default=0)
    current_balance = models.FloatField(verbose_name='当前余额')
    monthly_cost = models.FloatField(verbose_name='月租')
    comments = models.TextField(verbose_name='备注', blank=True)

    class Meta:
        verbose_name = "SIM卡信息"
        verbose_name_plural = verbose_name
