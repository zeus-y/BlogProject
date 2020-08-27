from django.contrib import admin
from .models import UserProfile,VerifyCodeEmail
# Register your models here.


class ComSetting(object):
	site_footer = '博客系统'
	site_title = '博客管理系统'


class CategoryXadmin(object):
	list_display = ['name', 'add_time']

admin.site.register(UserProfile)
admin.site.register(VerifyCodeEmail)