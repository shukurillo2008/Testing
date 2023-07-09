from rest_framework import serializers
from main import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'


class VarianSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Variant
        exclude = ['status', 'question']


class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='title')
    variants = VarianSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Question
        fields = '__all__'




class GroupSerializer(serializers.ModelSerializer):
    admin = serializers.SlugRelatedField(read_only = True, slug_field='username')
    
    class Meta:
        model = models.Group
        fields = '__all__'


class GroupListSerializer(serializers.ModelSerializer):
    admin = serializers.SlugRelatedField(read_only = True, slug_field='username')
    
    class Meta:
        model = models.Group
        fields = ['id','admin', 'title']


class QuestionListSerializer(serializers.ModelSerializer):

    class Meta:
            model = models.Question
            fields = ['id','title', 'category']


