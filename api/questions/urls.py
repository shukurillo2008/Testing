from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupsView.as_view()),    
    path('group/<int:pk>', views.GroupDetailView.as_view()),
    path('questions/', views.QuestionsListView.as_view()),
    path('question/<int:pk>', views.QuestionDetailView.as_view())
]