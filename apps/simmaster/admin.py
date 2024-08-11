from django.contrib import admin
from .models import MyUser, PlayInfo


# Register your models here.
class PlayInfoAdmin(admin.ModelAdmin):
    list_display = ['log', 'user_id', 'created']  # 需要展示出来的字段
    search_fields = ['log', 'created'] # 需要根据哪些字段搜索，搜索不能按外键字段搜索，否则报错
    list_filter = ['log', 'user_id', 'created'] # 按某个字段过滤，可以按外键，也可以指定多个字段

admin.site.register(PlayInfo, PlayInfoAdmin)

class MyUserInfoAdmin(admin.ModelAdmin):
    list_display = ['sex', 'birthday', 'rule', 'created']  # 需要展示出来的字段
    search_fields =  ['sex', 'birthday', 'rule', 'created'] # 需要根据哪些字段搜索，搜索不能按外键字段搜索，否则报错
    list_filter =  ['sex', 'birthday', 'rule', 'created'] # 按某个字段过滤，可以按外键，也可以指定多个字段

admin.site.register(MyUser, MyUserInfoAdmin)

