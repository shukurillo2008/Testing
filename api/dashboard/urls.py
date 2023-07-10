from django.urls import path
from . import views

urlpatterns = [
    path('question_groups/', views.QuestionGroupView.as_view()),
    path('question_group/<int:pk>/', views.QuestionGroupDetailView.as_view()),
    path('questions/', views.QuestionView.as_view()),
    path('question/<int:pk>', views.QuestionDetailView.as_view()),
    path('answer/<int:pk>', views.AnswerDetailView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view())
]