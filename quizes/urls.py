from django.urls import path
from .views import view_quiz, QuizDeleteView, update_quiz

app_name = 'quizes'
urlpatterns = [ path('quizes/<pk>/view', view_quiz, name='view_quiz'),
                path('quizes/<pk>/delete', QuizDeleteView.as_view(), name='delete_quiz'),
                path('quizes/<pk>/edit', update_quiz, name='update_quiz')
            ]
