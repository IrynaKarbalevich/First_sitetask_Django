from django import forms
from .models import *


class AddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'task': forms.Textarea(attrs={'cols': 50, 'rows': 10})
        }
