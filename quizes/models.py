from django.db import models
from myquiz.settings import AUTH_USER_MODEL


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=30)
    total_score = models.FloatField()
    creator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    date_added = models.DateField(auto_now_add=True)

    def __str(self):
        return "{0}--{1}".format(self.name, self.topic)

    def get_questions(self):
        return self.question_set.all()

