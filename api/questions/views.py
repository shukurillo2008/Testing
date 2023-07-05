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


class QuestionsListView(generics.ListAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category','group']
    search_fields = ['title']


class QuestionDetailView(APIView):
    def get(self, request, pk):
        question = models.Question.objects.get(pk=pk)
        answer = models.Variant.objects.filter(question = question)
        serializer_question = serializers.QuestionSerializer(question)
        serializer_answer = serializers.VarianSerializer(answer, many = True)

        return Response({
            'question': serializer_question.data,
            'answers': serializer_answer.data 
        })
    
    def post(self, request, pk):

        try:
            answer_id = request.POST.get('answer_id')
            user = request.user
            question = models.Question.objects.get(pk=pk)
            answer = models.Variant.objects.get(id=answer_id)

            try:
                models.UserAnAnswer.objects.get(user = user, question = question)
                return Response({
                    'message': 'You have already Answered'
                })

            except:
                if answer.status == True:
                    models.UserAnAnswer.objects.create(
                        user = user,
                        question = question,
                        status = True
                    )
                    return Response({'message':'your answer is True'})
                
                models.UserAnAnswer.objects.create(
                    user = user,
                    question = question,
                )    
                return Response({'message': 'Your answer is False'})
        
        except:
            return Response({
                'message': 'something went wrong =('
            })

