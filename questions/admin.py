from django.contrib import admin
from .models import Question,Choice, SubQuestion

class ChoiceInLine(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(SubQuestion)
