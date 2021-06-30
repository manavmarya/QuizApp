from django import forms
from .models import Quiz

class NewQuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        exclude = ['creator', 'date_added']

    def save(self, request, commit=True):
        quiz = super(forms.ModelForm, self).save(commit=False)
        quiz.creator = request.user
        if commit:
            quiz.save()
        return quiz