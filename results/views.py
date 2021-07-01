from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Result
from .forms import NewResultForm
from quizes.models import Quiz
from questions.models import Question, Choice, SubQuestion
from questions.forms import NewSubQuestionForm

def view_result(request, pk):
    result = Result.objects.get(pk=pk)
    return render(request, 'result.html', {'result': result })


def add_edit_result(request):
    if request.method == "POST":
        if (request.POST['result_pk'] != ""):
            subques_form = NewSubQuestionForm(request.POST)
            result_pk = request.POST['result_pk']
            quiz_pk = request.POST['quiz_pk']
            quiz = get_object_or_404(Quiz, pk=quiz_pk)
            question_pk = request.POST['question_pk']
            question = get_object_or_404(Question, pk=question_pk)
            choice_pk = request.POST['choice_pk']
            attempted_Choice = get_object_or_404(Choice, pk=choice_pk)
            result = get_object_or_404(Result, pk=result_pk)
            choice_correct = request.POST['choice_correct']
            if(choice_correct == 'False'):
                no = 0
            else:
                no = 1
            no_of_questions = quiz.question_set.count()
            result.score = result.score + no * result.quiz.total_score / no_of_questions
            result.save()
            SubQuestion(question=question, attempted_Choice=attempted_Choice, quiz=quiz, result=result).save()
            result_form = NewResultForm(instance=result)

        else:
            result_form = NewResultForm()
            subques_form = NewSubQuestionForm()
            quiz_pk = request.POST['quiz_pk']
            quiz = get_object_or_404(Quiz, pk=quiz_pk)
            score = 0
            student = request.user
            result = Result(quiz=quiz, student=student, score=score)
            result.save()

            return HttpResponse(result.pk)
    return render(request, 'quiz.html', {'result_form': result_form, 'subques_form' : subques_form })
