from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = (CommentInline, )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.unregister(User)
admin.site.unregister(Group)