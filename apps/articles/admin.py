from django.contrib import admin

from .models import Category,TagInfo,ArticleInfo,CommentInfo
# Register your models here.


class TagInfoXadmin(object):
	list_display = ['name', 'category','add_time']
	list_filter = ['category']

# class ArtTagXadmin(object):
# 	list_display = ['articleinfo', 'taginfo', 'add_time']


class ArticleInfoXadmin(object):
	list_display = ['title', 'click_num', 'cont_num', 'author', 'category','taginfo','image', 'add_time']
	style_fields = {'content': 'ueditor'}
	search_fields = ['title','author','category']
	list_editable = ['taginfo','category','image']
	# 添加附加选项表
	# class ArtTagInlines(object):
	# 	model = ArtTag
	# 	style = 'tab'
	# 	# exclude=['add_time']
	# 	extra = 2
	#
	# inlines = [ArtTagInlines]


admin.site.register(Category)
admin.site.register(TagInfo)
admin.site.register(ArticleInfo)
admin.site.register(CommentInfo)