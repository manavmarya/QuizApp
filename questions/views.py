from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
from .forms import NewQuestionsForm, NewChoiceFormSet
from quizes.models import Quiz
from django.views.generic.edit import DeleteView

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = "/profile/"

def view_question(request, pk):
    question = Question.objects.get(pk=pk)
    return render(request, 'question.html', {'question': question})

def register_ques_choice(request, quiz=Quiz.objects.get(pk=1)):
    if request.method == "POST":
        entry = request.POST.get("quiz_pk_add", False)
        if (entry):
            question_form = NewQuestionsForm()
            choice_form_set = NewChoiceFormSet()
            quiz = Quiz.objects.get(pk=request.POST['quiz_pk_add'])
            return render(request, "reg_question.html", context={'question_form': question_form, 'choice_formset': choice_form_set, 'quiz': quiz})
        question_form = NewQuestionsForm(request.POST)
        choice_form_set = NewChoiceFormSet(request.POST, prefix='choice_set')
        if question_form.is_valid():
            quiz_pk = request.POST['quiz_pk']
            quiz = Quiz.objects.get(pk=quiz_pk)
            question = question_form.save(request, quiz)
            if choice_form_set.is_valid():
                for choice_form in choice_form_set.forms:
                    choice_text = choice_form.cleaned_data.get('choice_text')
                    print(choice_text)
                    correct = choice_form.cleaned_data.get('correct')
                    print(correct)
                    question = question
                    print(question)
                    try:
                        Choice(choice_text=choice_text,correct=correct,question=question).save()
                    except Exception as e:
                        question.delete()
                        return HttpResponse(e)

            else:
                print('out')
                question.delete()
                return HttpResponse(choice_form_set.non_form_errors())
        else:
            print('bug')
            return HttpResponse(question_form.errors)
    question_form = NewQuestionsForm()
    choice_form_set = NewChoiceFormSet()
    return render(request, "reg_question.html", context={'question_form':question_form, 'choice_formset':choice_form_set, 'quiz':quiz})

def update_question(request, pk):
    context = {}
    obj = get_object_or_404(Question, id=pk)
    quiz = obj.quizes
    if ('pk_value' in request.POST):
        question_form = NewQuestionsForm(instance=obj)
        choice_form_set = NewChoiceFormSet(instance=obj)
    else:
        question_form = NewQuestionsForm(request.POST,instance=obj)
        choice_form_set = NewChoiceFormSet(request.POST, instance=obj)
    if question_form.is_valid():
        question = question_form.save(request, quiz)
        if choice_form_set.is_valid():
            i = 0
            for choice_form in choice_form_set.forms:
                if choice_form.is_valid():
                  if choice_form.cleaned_data.get('DELETE'):
                     print('check')
                     id = request.POST['choice_set-'+str(i)+'-id']
                     choice_inst = get_object_or_404(Choice, pk=id)
                     choice_inst.delete()
                     choice_form.instance.delete()
                  else :

                    question = question
                    choice_text = choice_form.cleaned_data.get('choice_text')
                    correct = choice_form.cleaned_data.get('correct')
                    id = request.POST['choice_set-' + str(i) + '-id']
                    if id == "":
                        choice_inst = Choice(choice_text=choice_text, correct=correct, question=question)
                        try:
                            choice_inst.save()
                        except Exception as e:
                            return HttpResponse(e)

                    else:
                        choice_inst, created = Choice.objects.get_or_create(pk=id, defaults={'choice_text': choice_text, 'correct': correct, 'question': question})
                        choice_inst.choice_text = choice_text
                        choice_inst.correct = correct
                        choice_inst.question = question
                        try:
                            choice_inst.save()
                        except Exception as e:
                            return HttpResponse(e)
                i = i + 1
        else:
            print('eck')
            return HttpResponse(choice_form_set.non_form_errors())

    context["question_form"] = question_form
    context["choice_formset"] = choice_form_set
    return render(request, "update_question.html", context)



