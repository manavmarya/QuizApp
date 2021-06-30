from django.test import TestCase
from .models import Question, Choice, SubQuestion
from .forms import NewQuestionsForm, NewChoiceFormSet, NewSubQuestionForm
from users.models import User, UserManager
from quizes.models import Quiz
from datetime import date

class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_manager = UserManager()

        user = user_manager.create_superuser('mmm@hh.com', 'kinshuk786')

        quiz = Quiz.objects.create(name="Science", topic="Physics", total_score=50, creator=user, date_added=date.fromisoformat('2019-12-04'))

        Question.objects.create(question_text='1+1', quiz=quiz)

    def question_name_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field('question_text').verbose_name
        self.assertEqual(field_label, 'Question text')

    def test_first_name_max_length(self):
        question = Question.objects.get(id=1)
        max_length = question._meta.get_field('question_text').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_question_text(self):
        question = Question.objects.get(id=1)
        expected_object_name = f'{question.question_text}'
        self.assertEqual(str(question), expected_object_name)
