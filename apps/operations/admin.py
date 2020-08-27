from django.contrib import admin

from .models import UserComment
# Register your models here.
class UserCommentXadmin(object):
	list_display = ['comment_man', 'comment_article', 'add_time']
admin.site.register(UserComment)
