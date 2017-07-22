from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth import urls as auth_urls
from app_article import views as article_views
from app_comments import views as comment_views

urlpatterns = [



    # test
    url(r'^test/', article_views.test),
    url(r'^reg/',login),
    url(r'^admin/', admin.site.urls),
    url(r'^$', article_views.index, name='index'),

    # app_article
    url(r'app_article/$', article_views.index, name='article_index'),
    url(r'article/(?P<pk>\d+)$', article_views.article_detail, name='article_detail'),

    # comment
    url(r'comment/add/(?P<pk>\d+)$', comment_views.comment_add, name='comment_add'),

    # upload
    url(r'^upload/', article_views.upload, name='blog_upload'),
    url(r'^qiniuupload/', article_views.qiniuupload, name='blog_upload'),
    url(r'^api/app_article/$', article_views.api_blog, name='api_blog'),

]
