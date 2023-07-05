from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupsView.as_view()),    
    path('group/<int:pk>', views.GroupDetailView.as_view()),
]