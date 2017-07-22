import datetime

from django.db import models


# Create your models here.
class Comment(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('app_article.Article')

    def __str__(self):
        return self.text[:100]
