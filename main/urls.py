from django.urls import path
from .views import HomePage, QuizDetailView

app_name = 'main'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz'),
]