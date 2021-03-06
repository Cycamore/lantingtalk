# Create your models here.

from __future__ import unicode_literals

from django import forms
from django.contrib import admin
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=50)
    # author = models.ForeignKey('Author')
    category = models.ForeignKey('Category')
    content = models.TextField()
    # score = models.IntegerField(null=True, default=0)  # 文章的打分
    created_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')

    # author= user

    def get_absolute_url(self):
        return reverse('article_detail', args={self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    gender_choice = ((1, 'male'), (2, 'female'))
    name = models.CharField(unique=True, max_length=50)
    qq = models.CharField(max_length=10, blank=True)
    addr = models.TextField(blank=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=gender_choice, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # 自定义 get_absolute_url 方法
        # 记得从 django.urls 中导入 reverse 函数
        return reverse('article_detail', kwargs={'pk': self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=30)
    head_img = models.FileField(upload_to='./upload')

    def __str__(self):
        return self.username


class UserForm(forms.Form):
    username = forms.CharField()
    head_img = forms.FileField()
