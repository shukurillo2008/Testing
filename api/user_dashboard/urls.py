from django.urls import path
from . import views

urlpatterns = [
    path('my_question_groups/', views.MyGroupsView.as_view()),
    path('my_groups_detail/<int:pk>', views.MyGroupDetailView.as_view()),    
]