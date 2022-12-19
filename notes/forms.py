from django import forms
from django.core.exceptions import ValidationError
from .models import Notes
from django.forms import TextInput, Textarea


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control mb-3",
                'style': 'max-width : 600px',
                'placeholder':'Write Title Here!'
            }),
            'text': Textarea(attrs={
                'class': "form-control mb-3",
                'style': 'max-width : 600px',
                'rows': "5",
                'placeholder': 'Write Note Here!'
            })

        }
