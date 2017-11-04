from django import template
from app_article.models import Article

register = template.Library()


@register.simple_tag
def get_recent_article(num=5):
    return Article.objects.all().order_by('-created_time')[:num]
