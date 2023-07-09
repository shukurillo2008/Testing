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
        # question_list = []

        # for i in question:
        #     variant = []
        #     question_variants = models.Variant.objects.filter(question=i)
        #     for x in question_variants:
        #         variant.append(x)
        #     i.varyants = variant
        #     question_list.append(i)
       
        serializer_group = serializers.GroupSerializer(group)
        serializer_question = serializers.QuestionSerializer(question, many = True)

        return Response({
            'group': serializer_group.data,
            'questions': serializer_question.data
        })
    
    def post(self, request, pk):
        try:
            question_id = request.POST.get('question_id')
            answer_id = request.POST.get('answer_id')
            group = models.Group.objects.get(pk=pk)
            question = models.Question.objects.get(id=question_id)
            answer = models.Variant.objects.get(id=answer_id)
            try:
                answer_g = models.UserAnswerGroup.objects.get(user=request.user, group=group)
                try:
                    models.UserAnAnswer.objects.get(user=request.user, question = question)
                    return Response({
                      'message': 'You have already Answered'
                    })
                except:
                    if answer.status == True:
                        models.UserAnAnswer.objects.create(
                            user=request.user, question=question, answer_group=answer_g, status = True
                            )
                        answer_g.true_answer +=1
                        answer_g.save()
                        return Response({"message": "your answer is correct"})
                    
                    models.UserAnAnswer.objects.create(
                        user = request.user, question=question, answer_group=answer_g
                        )
                    answer_g.false_answer -=1
                    answer_g.save()
                    print(False)
                    return Response({"message":"your answer is False"})
                    
            except:
                answer_group = models.UserAnswerGroup.objects.create(
                    user = request.user,
                    group = group
                )
                try:
                    models.UserAnAnswer.objects.get(user=request.user, question = question)
                    return Response({
                      'message': 'You have already Answered'
                    })
                except:
                    if answer.status == True:
                        models.UserAnAnswer.objects.create(
                            user=request.user, question=question, answer_group=answer_group, status = True
                            )
                        answer_group.true_answer +=1
                        answer_group.save()
                        return Response({"message": "your answer is correct"})
                    
                    models.UserAnAnswer.objects.create(
                        user = request.user, question=question, answer_group=answer_group
                        )
                    answer_group.false_answer -=1
                    answer_group.save()
                    return Response({"message":"your answer is False"})

        except:
            return Response({
              'message': 'Something went wrong =('
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
        serializer_question = serializers.QuestionSerializer(question)

        return Response({
            'question': serializer_question.data,
        })
    
    def post(self, request, pk):

        try:
            answer_id = request.POST.get('answer_id')
            question = models.Question.objects.get(pk=pk)
            answer = models.Variant.objects.get(id=answer_id)

            try:
                models.UserAnAnswer.objects.get(user = request.user, question = question)
                return Response({
                    'message': 'You have already Answered'
                })

            except:

                try:
                    answer_group = models.UserAnswerGroup.objects.get(user=request.user, group = question.group)
                    if answer.status == True:
                        models.UserAnAnswer.objects.create(
                            user = request.user,
                            question = question,
                            status = True
                        )
                        answer_group.true_answer += 1
                        answer_group.save()
                        return Response({'message':'your answer is True'})
                    
                    models.UserAnAnswer.objects.create(
                        user = request.user,
                        question = question,
                    )
                    answer_group.false_answer += 1
                    answer_group.save()    
                    return Response({'message': 'Your answer is False'})
                
                except:
                    answer_group = models.UserAnswerGroup.objects.create(user=request.user, group = question.group)
                    if answer.status == True:
                        models.UserAnAnswer.objects.create(
                            user = request.user,
                            question = question,
                            status = True
                        )
                        answer_group.true_answer += 1
                        answer_group.save()
                        return Response({'message':'your answer is True'})
                    
                    models.UserAnAnswer.objects.create(
                        user = request.user,
                        question = question,
                    )
                    answer_group.false_answer += 1
                    answer_group.save()    
                    return Response({'message': 'Your answer is False'})
       
        except:
            return Response({
                'message': 'something went wrong =('
            })

