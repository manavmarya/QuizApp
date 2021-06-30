from django.db import models
from quizes.models import Quiz
from myquiz.settings import AUTH_USER_MODEL

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    score = models.FloatField()

    def __str__(self):
        return "{0} scored {1} out of {2} in Quiz '{3}'".format(self.student.name, self.score, self.quiz.total_score, self.quiz)
