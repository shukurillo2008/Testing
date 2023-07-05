from rest_framework.response import Response
from main import models
from rest_framework import generics, filters
from rest_framework.views import APIView
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


class MyAnAnswersView(APIView):

    def get(self, request):
        answers = models.UserAnAnswer.objects.filter(user = request.user)
        serializer = serializers.AnAnswerSerializer(answers, many=True)
        return Response(serializer.data)
    

class MyAnAnswerDetailView(APIView):

    def get(self, request, pk):
        answer = models.UserAnAnswer.objects.get(pk = pk)
        ser_answer = serializers.AnAnswerSerializer(answer)
        ser_question = serializers.QuestionSerializer(answer.question)

        return Response({
            'question':ser_question.data,
            'answer':ser_answer.data, 
            })


