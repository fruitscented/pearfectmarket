from ckeditor.fields import RichTextField
from django import forms
from django.db.models import ManyToManyField
from django.forms import SlugField
from .models import Contact, Subtag


class PostForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'