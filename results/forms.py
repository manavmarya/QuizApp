from django import forms
from .models import Result

class NewResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = "__all__"