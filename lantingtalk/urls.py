from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from app_article.serializers import *
from app_article import views as article_view
from django.urls import reverse
from app_comment import views as app_comments_views


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'articles', ArticleViewSet)

urlpatterns = [
    url(r'^$', article_view.IndexView.as_view(), name='index'),
    url(r'articles/(?P<pk>\d+)$', article_view.article_detail, name='article_detail'),
    url(r'articles/(?P<pk>\d+)/comments', app_comments_views.comments, name='article_comments'),
    url(r'test', article_view.test, name='myurl'),
    # url(r'^', article_list),
    # # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # # api
    # url(r'^api/article/$', article_views.api_article, name='api_blog'),

    # test
    # url(r'^test/', article_views.test),
    # url(r'^reg/', login),
    url(r'^admin/', admin.site.urls),
    # # url(r'^$', article_views.index, name='index'),
    # url(r'^api/',include('rest_framework.urls',namespace='rest_framework')),
    #
    #
    #
    # # app_article
    # url(r'app_article/$', article_views.index, name='article_index'),
    # # comment
    #
    # # upload
    # url(r'^upload/', article_views.upload, name='blog_upload'),
    # url(r'^qiniuupload/', article_views.qiniuupload, name='blog_upload'),

]
