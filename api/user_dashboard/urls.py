from django.urls import path
from . import views_answers, views_group, views_question

urlpatterns = [
    path('my_question_groups/', views_group.MyGroupsView.as_view()),
    path('my_groups_detail/<int:pk>', views_group.MyGroupDetailView.as_view()),
    path('my_questions/', views_question.MyQuestionsView.as_view()),
    path('my_questions_detail/<int:pk>', views_question.MyQuestionDetailView.as_view()),
    path('my_ananswers/', views_answers.MyAnAnswersView.as_view()),
    path('my_ananswer_detail/<int:pk>', views_answers.MyAnAnswerDetailView.as_view()),
    path('my_answer_groups/', views_answers.MyAnswerGroupView.as_view()),
    path('my_answer_group/<int:pk>', views_answers.MyAnswerGroupDetailView.as_view()),
]