from django.urls import path,include

urlpatterns = [
    path('test/',include('api.questions.urls')),
    path('dashboard/',include('api.dashboard.urls')),
    path('user_dashboard/',include('api.user_dashboard.urls')),
]