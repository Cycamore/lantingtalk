"""lantingtalk URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from article import views as blog_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # index
    url(r'^$', blog_views.index, name='blog_index'),
    # detail
    url(r'^article/(?P<pk>\d+)$',blog_views.article_detail,name='article_detail'),


    # upload
    url(r'^upload/', blog_views.upload, name='blog_upload'),
    url(r'^qiniuupload/', blog_views.qiniuupload, name='blog_upload'),
    url(r'^api/article/$', blog_views.api_blog, name='api_blog'),

]
