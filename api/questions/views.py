from rest_framework.response import Response
from main import models
from rest_framework import generics, filters
from rest_framework.views import APIView
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend


class GroupsView(generics.ListAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['admin']
    search_fields = ['title', 'admin__username']


class GroupDetailView(APIView):

    def get(self, request, pk):
        group = models.Group.objects.get(pk=pk)
        question = models.Question.objects.filter(group = group)
        serializer_group = serializers.GroupSerializer(group)
        serializer_question = serializers.QuestionSerializer(question, many = True)

        return Response({
            'group': serializer_group.data,
            'questions': serializer_question.data
        })
