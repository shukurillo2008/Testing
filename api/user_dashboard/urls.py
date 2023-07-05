from django.urls import path
from . import views

urlpatterns = [
    path('my_question_groups/', views.MyGroupsView.as_view()),
    path('my_groups_detail/<int:pk>', views.MyGroupDetailView.as_view()),
    path('my_questions/', views.MyQuestionsView.as_view()),
    path('my_questions_detail/<int:pk>', views.MyQuestionDetailView.as_view()),
    # path('my_answers/', views.MyAnswersView.as_view()),
    # path('my_answers_detail/<int:pk>', views.MyAnswerDetailView.as_view()),
]