from articles.models import Category
from xadmin.views import BaseAdminView, CommAdminView
from .models import UserProfile,VerifyCodeEmail
import xadmin


# class BaseSetting(BaseAdminView):
# 	pass

# class UserAdmin(object):
#     style_fields = {"content": "ueditor"}
# xadmin.site.register(UserProfile, UserAdmin)


class ComSetting(object):
	site_footer = '博客系统'
	site_title = '博客管理系统'


xadmin.site.register(CommAdminView, ComSetting)


class CategoryXadmin(object):
	list_display = ['name', 'add_time']



xadmin.site.register(Category, CategoryXadmin)

