from django.contrib import admin
from .models import SimList


# Register your models here.
class SimListAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'user', 'current_balance', 'monthly_cost', 'comments']  # 需要展示出来的字段
    search_fields = ['phone_number', 'sim_number', 'carrier', 'location',
                     'current_balance', 'monthly_cost']  # 需要根据哪些字段搜索，搜索不能按外键字段搜索，否则报错
    list_filter = ['user', 'carrier']  # 按某个字段过滤，可以按外键，也可以指定多个字段


admin.site.register(SimList, SimListAdmin)
