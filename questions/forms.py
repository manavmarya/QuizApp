from django import forms
from django.forms import inlineformset_factory
from .models import Question, Choice, SubQuestion
from django.core.exceptions import ValidationError

class NewQuestionsForm(forms.ModelForm):

    class Meta:
        model = Question
        exclude = ['quizes']
        widgets = {'question_text': forms.Textarea(attrs={'rows': 5, 'cols': 25})}

    def save(self, request, quiz, commit=True):
        question = super(forms.ModelForm, self).save(commit=False)
        question.quizes = quiz
        if commit:
            question.save()
        return question

class NewChoiceFormSet(inlineformset_factory(Question, Choice, can_delete=True, max_num=4, min_num=1, exclude = ('quizes','delete'), extra=0, widgets = {'choice_text' : forms.Textarea(attrs={'rows':2, 'cols':33 }) })):
    def clean(self):
       super(NewChoiceFormSet, self).clean()
       is_correct = 0
       i = 0
       for form in self.forms:
           if not form.is_valid():
               continue
           if form.cleaned_data and not form.cleaned_data.get('DELETE'):
               if (form.cleaned_data.get('correct')):
                   is_correct=1
               print(form.cleaned_data)
               #if(i>0):
               # name = "choice_set-" + str(i) + "-correct"
               # if( name in )
       if (is_correct == 0):
            raise ValidationError('No correct choice')



class NewSubQuestionForm(forms.ModelForm):
    class Meta:
        model = SubQuestion
        fields = ['attempted_Choice']

    def save(self, request, question, quiz, result, attempted_Choice, commit=True):
        sub_ques = super(forms.ModelForm, self).save(commit=False)
        sub_ques.question = question
        sub_ques.quiz = quiz
        sub_ques.result = result
        sub_ques.attemptedChoice = attempted_Choice
        if commit:
            sub_ques.save()
        return sub_ques