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
        true_answer = models.Variant.objects.get(question = answer.question, status = True)
        ser_answer = serializers.AnAnswerSerializer(answer)
        ser_question = serializers.QuestionSerializer(answer.question)
        ser_answer_true = serializers.VarianSerializer(true_answer)

        return Response({
            'question':ser_question.data,
            'your_answer':ser_answer.data,
            'true_answer':ser_answer_true.data,
            })


class MyAnswerGroupView(APIView):

    def get(self, request):
        answer_group = models.UserAnswerGroup.objects.filter(user = request.user)
        ser_answer_group = serializers.AnswerGroupSerializer(answer_group, many=True)

        return Response({
            'answer_group':ser_answer_group.data
        })


class MyAnswerGroupDetailView(APIView):

    def get(self, request, pk):
        answer_group = models.UserAnswerGroup.objects.get(pk = pk)
        ser_your_answer = serializers.AnswerGroupSerializer(answer_group) 
        ser_answer_group = serializers.GroupMydetailsSerializer(answer_group.group)
        ser_question = serializers.AnAnswerSerializer(answer_group.ananswer, many = True)

        return Response({
            'your':ser_your_answer.data,
            'answer_group':ser_answer_group.data,
            'answers':ser_question.data
        })