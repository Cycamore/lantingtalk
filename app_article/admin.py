from app_article.models import *

# Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(User)