from ckeditor.fields import RichTextField
from django import forms
from django.db.models import ManyToManyField
from django.forms import SlugField
from .models import Question


class QForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

