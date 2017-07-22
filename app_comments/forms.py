from  django import forms
from django.forms import SelectDateWidget

from .models import Comment


class CommentForm(forms.Form):
    user = forms.CharField(max_length=100)
    text = forms.CharField(max_length=400)


class TestForm(forms.Form):
    SEX_CHOICES = (
        ('male', '男'),
        ('female', '女')
    )

    BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984')

    nickname = forms.CharField(max_length=20, label="nick",
                               widget=forms.TextInput(attrs={'class': 'special', 'id': 'nick'}),
                               error_messages={'required': u'别名不能为空'})
    username = forms.CharField(label="用户名", error_messages={'required': u'用户名不能为空'})
    password = forms.CharField(label="密码", widget=forms.PasswordInput)
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=SEX_CHOICES, label="性别")
    email = forms.EmailField(label="邮箱", error_messages={'required': u'邮箱不能为空', 'invalid': u'请输入正确的邮箱'})
    phone = forms.CharField(required=False, label="手机号")
    birthday = forms.DateField(widget=forms.SelectDateWidget(empty_label='empty label'),label='select data',error_messages={'invalid':u'invalid'})
    cf=forms.ChoiceField(widget=forms.RadioSelect,choices=SEX_CHOICES,required=False,label='choice',initial='male')
    data=forms.DateTimeField(widget=forms.TextInput,)
