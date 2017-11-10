from django.core.files import File

from app_article.models import Article, Author, Tag, User,Category
from django.contrib import admin


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_time',)
    # list_editable = ('content',)
    list_display_links = (['title'])
    list_per_page = 15
    search_fields = ['title','content']
    list_filter = ['created_time']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Category)
