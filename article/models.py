# Create your models here.

from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','author','content')



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


