from django.db import models
from django.core.exceptions import ValidationError
from quizes.models import Quiz
from results.models import Result

class Question(models.Model):
    question_text = models.TextField(max_length=1000)
    quizes = models.ForeignKey(Quiz, on_delete=models.CASCADE, )

    def __str__(self):
        return str(self.question_text)

    def get_choices(self):
        return self.choice_set.all()

    def save(self):
        if self.quizes.question_set.count() <= 10:
            super(Question, self).save()
        else:
            raise ValidationError(f'{self.quizes.name} has already 10 questions. No more are allowed.')

class Choice(models.Model):
    choice_text = models.TextField(max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(self.choice_text)

    def save(self):
        if self.question.choice_set.count() <= 4:
            super(Choice, self).save()
        else:
            raise Exception('Question already has 4 choices. No more are allowed.')

class SubQuestion(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    attempted_Choice = models.OneToOneField(Choice, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)