from django.db import models
from django.contrib.auth.models import User 


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Group(models.Model):
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='questions')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Variant(models.Model):
    answer = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='variants')
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.question.title
    

class UserAnswerGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    true_answer = models.PositiveIntegerField(default=0)
    false_answer = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username
    

class UserAnAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer_group = models.ForeignKey(UserAnswerGroup, on_delete=models.SET_NULL, null=True, related_name='ananswer')
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.question.title
    
