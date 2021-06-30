from django.urls import path
from .views import register_ques_choice, view_question, QuestionDeleteView, update_question

app_name = 'questions'
urlpatterns = [ path('questions/<pk>/', view_question, name='view_question'),
                path('profile/questions/', register_ques_choice, name='register_ques_choice'),
                path('questions/<pk>/delete', QuestionDeleteView.as_view(), name='delete_ques'),
                path('questions/<pk>/edit', update_question, name='update_question')
            ]