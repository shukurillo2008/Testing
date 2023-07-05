from django.urls import path,include

urlpatterns = [
    path('',include('api.questions.urls')),
    path('',include('api.dashboard.urls'))
]