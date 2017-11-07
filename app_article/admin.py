from app_article.models import Article, Author, Tag, User
from django.contrib import admin


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_time',)
    # list_editable = ('content',)
    list_display_links = (['title'])
    list_per_page = 5


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(User)
