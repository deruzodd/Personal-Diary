from django import forms
from tinymce.widgets import TinyMCE
from .models import Moods

class EntryCreationForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=4, label='Entry title',
        widget=forms.TextInput(attrs={
            'placeholder': 'Dear Diary...',
            'class': 'form-control form-control-lg bg-basic',
    }))
    location = forms.CharField(max_length=200, label='Where was this entry made?', required=False)
    mood = forms.ChoiceField(label='How is your mood?', choices=Moods.choices,
        widget=forms.Select(attrs={
            'class': 'form-control mood-input ms-4 mt-2 p-1 bg-basic',
    }))

class EditorForm(forms.Form):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
