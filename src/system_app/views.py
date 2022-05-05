from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, CommentThreadSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleSerializer


class ArticleCreateView(generics.CreateAPIView):
    pass
    # queryset = Article.objects.all().order_by('id')
    # serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(response_comment=None)

    def get_queryset(self):
        article_id = self.kwargs.get('article_id')
        article = get_object_or_404(Article, id=article_id)
        queryset = Comment.objects.filter(article=article, response_comment=None)
        return queryset

    def perform_create(self, serializer):
        article = get_object_or_404(Article, id=self.kwargs['article_id'])
        serializer.save(article=article)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CommentSerializer(instance)
        return Response(serializer.data)


class CommentThreadAPIView(RetrieveAPIView):
    queryset = Comment.objects.filter(nested_lvl=3)
    serializer_class = CommentThreadSerializer
