

from django.db import models


class Article(models.Model):
    content = models.TextField(max_length=1000)
    datetime_publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    response_comment = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, default=None)
    content = models.TextField(max_length=200)
    level_nest = models.PositiveSmallIntegerField(default=1, blank=True)
    datetime_publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.response_comment}, f{self.content}" if self.response_comment else f"{self.content}"