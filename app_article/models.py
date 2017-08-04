# Create your models here.

from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10,blank=True)
    addr = models.TextField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author')
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    created_time=models.DateTimeField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

        # 自定义 get_absolute_url 方法
        # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','author','created_time','title', 'content')
    list_editable = ('content',)
    list_per_page = 5



class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=30)
    head_img = models.FileField(upload_to='./upload')

    def __str__(self):
        return self.username


# 上传表单
class UserForm(forms.Form):
    username = forms.CharField()
    head_img = forms.FileField()
