import json
import uuid

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404

from article.models import *


# Create your views here.
def index(request):
    article = Article.objects.all()
    return render(request, 'blog/index.html', context={'article': article})


def article_detail(request, pk):
    art = get_object_or_404(Article, pk=pk)
    return render(request,'blog/article_detail.html',context={'art':art})



# 文件上传
def upload(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            head_img = uf.cleaned_data['head_img']
            # 写入数据库
            user = User()
            user.username = username
            user.head_img = head_img
            user.save()
            return HttpResponse('upload ok')
    else:
        uf = UserForm()
    return render_to_response('blog/upload.html', {'uf': uf})


# 上传至七牛云
def qiniuupload(request):
    import qiniu
    ACCESS_KEY = 'MMf7l_IkGqABQYjanykyLtnXZIA0QGITya-bPaxZ'
    SECRET_KEY = '8Ua7DPHhd-7U8yx-ySao16LbPsgINvk3tMvLmbIV'
    BUCKET_NAME = 'cycamore'
    key = str(uuid.uuid1()).replace('-', '')  # 这里使用uuid作为保存在七牛里文件的名字。并去掉了uuid中的“-”
    q = qiniu.Auth(ACCESS_KEY, SECRET_KEY)
    token = q.upload_token(BUCKET_NAME, key, 7200, {'returnUrl': 'http://127.0.0.1:8000/',
                                                    'returnBody': '{"name": $(fname), "key": $(key)}',
                                                    'mimeLimit': 'image/jpeg;image/png'})
    return render_to_response('blog/qiniuupload.html', {'token': token, 'key': key})


# 将blog生成json返回给客户端
def api_blog(request):
    article = Article.objects.all()
    data = serializers.serialize('json', article)
    return HttpResponse(data)
