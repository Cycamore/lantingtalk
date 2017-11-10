import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from app_article.models import Article
from .forms import *
from .models import *


# Create your views here.
def comments(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user.username
        text = str(request.POST['text'])
        if user == "" or text == "":
            return redirect(article)
        else:
            comment = Comment(user=user, text=text)
            comment.article = article
            comment.created_time = datetime.datetime.now()
            comment.save()
            return redirect(article)

            # comment.app_article=app_article
            # comment.save()
    return redirect(article)
    # return redirect(app_article)
    # else:
    #     # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
    #     # 因此我们传了三个模板变量给 article_detail.html，
    #     # 一个是文章（app_article），一个是评论列表，一个是表单 form
    #     # 注意这里我们用到了 app_article.comment_set.all() 方法，
    #     # 这个用法有点类似于 Article.objects.all()
    #     # 其作用是获取这篇 app_article 下的的全部评论，
    #     # 因为 Article 和 Comment 是 ForeignKey 关联的，
    #     # 因此使用 app_article.comment_set.all() 反向查询全部评论。
    #     # 具体请看下面的讲解。
    #     comment_list = app_article.comment_set.all()
    #     context = {'app_article': app_article,
    #                'form': form,
    #                'comment_list': comment_list
    #                }
    #     return render(request, 'app_article/article_detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    # return redirect(app_article)
