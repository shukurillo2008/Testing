from rest_framework.response import Response
from main import models
from rest_framework import generics, filters
from rest_framework.views import APIView
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q



class MyQuestionsView(APIView):
    
    def get(self, request):
        search = request.GET.get('search')
        if search:
            questions = models.Question.objects.filter(Q(title__icontains= search)|Q(category__title__icontains = search)|Q(group__title__icontains=search),group__admin = request.user)
        questions = models.Question.objects.filter(group__admin = request.user)
        serializer = serializers.QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            title = request.POST.get('title')
            body = request.POST.get('body')
            category = request.POST.get('category')
            group = request.POST.get('group')
            
            try:
                question = models.Question.objects.get(title = title)
                return Response({'message':'Already created like this Question'})
            
            except:
                models.Question.objects.create(
                    title = title,
                    body = body,
                    category = category,
                    group = models.Group.objects.get(title = group),
                    admin = request.user
                )
                return Response({'message': 'Successfully created'})
        
        except:
            return Response({'message':'something went wrong =)'})
        

class MyQuestionDetailView(APIView):

    def get(self, request, pk):
        question = models.Question.objects.get(pk = pk)
        ser_question = serializers.QuestionSerializer(question)
        ser_group = serializers.GroupSerializer(question.group)

        return Response({
            'question':ser_question.data, 
            'group':ser_group.data
            })
    
    def post(self, request, pk):
        try:
            question = models.Question.objects.get( pk = pk )
            title = request.POST.get('title')
            body = request.POST.get('body')
            category = request.POST.get('category')
            group = request.POST.get('group')
            
            if request.user == question.admin:
                question.admin = request.user
                question.title = title
                question.body = body
                question.category = category
                question.group = models.Group.objects.get(title = group)
                question.save()
                
                return Response({'message':'Successfully updated'})
            
            return Response({'mesage':'you have not permissions to this group'})
        
        except:
            return Response({'message':'something went wrong =)'})
        