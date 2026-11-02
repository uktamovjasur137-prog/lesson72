from django.contrib import admin
from .models import Profile, Science, Quiz, Question, QuestionVariant, Answer

admin.site.register(Profile)
admin.site.register(Science)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuestionVariant)
admin.site.register(Answer)