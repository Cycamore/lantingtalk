from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article
from .forms import *


# Create your views here.
def article_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(article)
        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 article_detail.html，
            # 一个是文章（article），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 article.comment_set.all() 方法，
            # 这个用法有点类似于 Article.objects.all()
            # 其作用是获取这篇 article 下的的全部评论，
            # 因为 Article 和 Comment 是 ForeignKey 关联的，
            # 因此使用 article.comment_set.all() 反向查询全部评论。
            # 具体请看下面的讲解。
            comment_list = article.comment_set.all()
            context = {'article': article,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/article_detail.html', context=context)
