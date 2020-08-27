"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include

from django.contrib import admin
from django.urls import re_path

from users.views import index,search,user_active,page_not_found
from articles.views import list_detail,article_detail
from operations.views import user_comment,add_Marticle
from MyBlog import settings
from django.views.static import serve
import xadmin
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',index,name='index'),
	url(r'^admin/',admin.site.urls),
	url(r'^ueditor/',include('DjangoUeditor.urls')),
	url(r'^mysite/',xadmin.site.urls),
	url(r'^user/',include('users.urls')),
	url(r'^list/(\w+)/$',list_detail,name='list'),
	re_path('^detail/(\d+)/$',article_detail,name='detail'),
	url(r'^search/$',search,name='search'),
	url(r'^user_active/(\w+)/$',user_active,name='user_active'),
	url(r'^user_comment/(\d+)/$',user_comment,name='user_comment'),
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
	url(r'^media/(?P<path>.*)$' , serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
	# url(r'^add_article/$', add_Marticle, name='add_article')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = page_not_found # 改动2

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)