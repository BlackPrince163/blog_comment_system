from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    comments = SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'content', 'comments')

    def get_comments(self, obj):
        queryset = Comment.objects.filter(article=obj, response_comment=None)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'response_comment', 'level_nest', 'replies')

    def get_replies(self, obj):
        queryset = Comment.objects.filter(response_comment=obj.id, level_nest__lte=3)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data

    def create(self, validated_data):
        try:
            response_comments = validated_data.pop('response_comments')
            child_lvl = response_comments.nested_lvl + 1
            comment = Comment.objects.create(level_nest=child_lvl, response_comment=response_comments, **validated_data)
        except KeyError:
            comment = Comment.objects.create(**validated_data)
        return comment


class CommentThreadSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'replies')

    def get_replies(self, obj):
        queryset = Comment.objects.filter(response_comment=obj)
        serializer = CommentThreadSerializer(queryset, many=True)
        return serializer.data
