from django.shortcuts import render, get_object_or_404
from quizes.models import Quiz
from .forms import NewQuizForm
from django.views.generic.edit import DeleteView

class QuizDeleteView(DeleteView):
    model = Quiz
    success_url = "/profile/"

def view_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz.html', {'quiz': quiz })


def update_quiz(request, pk):
    context = {}
    obj = get_object_or_404(Quiz, id=pk)
    quiz_form = NewQuizForm(request.POST or None, instance=obj)
    if quiz_form.is_valid():
        quiz_form.save(request)
    context["quiz_form"] = quiz_form
    context["quiz"] = obj
    return render(request, "update_quiz.html", context)


