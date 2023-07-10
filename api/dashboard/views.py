from rest_framework.response import Response
from main import models
from rest_framework import generics, filters
from rest_framework.views import APIView
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


class QuestionGroupView(generics.ListCreateAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.QuestionGroupListSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['admin', 'created']
    search_fields =['title']


class QuestionGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.QuestionGroupDetailSerializer


class QuestionView(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionListSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['group', 'category', 'created']
    search_fields = ['title']


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestonDetailSerializer


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Variant.objects.all()
    serializer_class = serializers.AnswerDetailSerializer



class UserListView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['is_superuser']
    search_fields = ['username']


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer

    