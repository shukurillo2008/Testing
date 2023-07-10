from  rest_framework import serializers
from main import models


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Variant
        fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        exclude = ['created']


class AnswerDetailSerializer(serializers.ModelSerializer):
    question = QuestionListSerializer(read_only=True)

    class Meta:
        model = models.Variant
        fields = '__all__'


class QuestonDetailSerializer(serializers.ModelSerializer):
    variants = AnswerSerializer(many = True, read_only = True)

    class Meta:
        model = models.Question
        fields = '__all__'

    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['username', 'id', 'password', 'is_superuser']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = '__all__'

    
class QuestionGroupListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Group
        fields = ['id','admin', 'title', 'body', 'questions']


class QuestionGroupDetailSerializer(serializers.ModelSerializer):
    questions = QuestonDetailSerializer(many = True, read_only = True)
    
    class Meta:
        model = models.Group
        fields = '__all__'
        

