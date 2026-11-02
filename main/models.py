from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    about = models.TextField()
    profile_image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.user.username


class Science(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=500)

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question_text


class QuestionVariant(models.Model):
    variant_text = models.CharField(max_length=500)
    status = models.BooleanField(default=False)

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='variants')
    
    def __str__(self):
            return self.variant_text

class Answer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='answers')

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    variant = models.ForeignKey(QuestionVariant, on_delete=models.CASCADE, related_name='answers')
