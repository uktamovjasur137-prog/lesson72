from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quiz, Science
from django.utils import timezone

class HomePage(ListView):
    model = Quiz
    template_name = 'index.html'
    context_object_name = 'quizzes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sciences'] = Science.objects.all()
        context['now'] = timezone.now()
        return context

    
class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'main/quiz.html'
    context_object_name = 'quiz'