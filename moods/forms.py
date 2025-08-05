from django import forms
from .models import MoodEntry

class MoodEntryForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood', 'emotion_tags']
        widgets = {
            'mood': forms.NumberInput(attrs={'min':1, 'max': 10}),
            'emotion_tags': forms.TextInput(attrs={'placeholder': 'e.g. happy, focused'}),
        }