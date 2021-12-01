from django.db import models
from accounts.models import User
# Create your models here.
class QuizModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(default=0, help_text='Duration of the quiz')
    user = models.ManyToManyField(to=User, related_name='Quizzes')

    def __str__(self):
        return self.title


class QuestionModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    quiz = models.ForeignKey(to=QuizModel, on_delete=models.CASCADE,
     related_name='questions', verbose_name='quiz for question')

    def __str__(self):
        return self.question

