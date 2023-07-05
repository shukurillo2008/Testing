from rest_framework.response import Response
from main import models
from rest_framework import generics, filters
from rest_framework.views import APIView
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend


class MyGroupsView(APIView):

    def get(self, request):
        groups = models.Group.objects.filter(admin = request.user)
        serializer = serializers.GroupSerializer(groups, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
        try:            
            title = request.POST.get('title')
            body = request.POST.get('body')
            
            try:
                group = models.Group.objects.get(title = title)
                return Response({'message':'Already created like this Group'})
            
            except:
                models.Group.objects.create(
                    title = title,
                    body = body,
                    admin = request.user
                )
                return Response({'message': 'Successfully created'})
        
        except:
            return Response({'message':'something went wrong =)'})
        

class MyGroupDetailView(APIView):

    def get(self, request, pk):
        group = models.Group.objects.get(pk = pk)
        question = models.Question.objects.filter(group = group)
        ser_question = serializers.QuestionListSerializer(question, many=True)
        ser_group = serializers.GroupSerializer(group)

        return Response({
            'group':ser_group.data, 
            'questions':ser_question.data
            })
    
    def post(self, request, pk):
        try:
            group = models.Group.objects.get( pk = pk )
            title = request.POST.get('title')
            body = request.POST.get('body')
            
            if request.user == group.admin:
                group.admin = request.user
                group.title = title
                group.body = body
                group.save()
                
                return Response({'message':'Successfully updated'})
            
            return Response({'mesage':'you have not permissions to this group'})
        
        except:
            return Response({'message':'something went wrong =)'})
    
    def delete(self, request, pk):
        try:
            group = models.Group.objects.get( pk = pk )
            if request.user == group.admin:
                group.delete()
                return Response({'message':'Successfully deleted'})
            
            return Response({'mesage':'you have not permissions to this group'})
        
        except:
            return Response({'message':'something went wrong =)'})
        

class MyQuestionsView(APIView):
    
    def get(self, request):
        questions = models.Question.objects.filter(group__admin = request.user)
        serializer = serializers.QuestionListSerializer(questions, many=True)
        return Response(serializer.data)