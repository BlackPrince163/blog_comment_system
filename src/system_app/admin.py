from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
admin.site.unregister(User)
admin.site.unregister(Group)