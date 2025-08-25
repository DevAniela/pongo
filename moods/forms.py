from django import forms
from .models import MoodEntry

EMOTION_TAG_OPTIONS = {
    'happy': ['joyful', 'peaceful', 'excited'],
    'angry': ['frustrated', 'furious', 'annoyed'],
    'sad': ['gloomy', 'lonely', 'depressed'],
    'fear': ['anxious', 'nervous', 'powerless'],
    'disgust': ['revolted', 'embarrassed', 'judgemental'],
    'surprise': ['shocked', 'curious', 'amazed'],
}

class MoodEntryForm(forms.ModelForm):    
    class Meta:
        model = MoodEntry
        fields = ['happy', 'angry', 'sad', 'fear', 'disgust', 'surprise']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for emotion in ['happy', 'angry', 'sad', 'fear', 'disgust', 'surprise']:
            self.fields[emotion].initial = 4
        
        for emotion, tags in EMOTION_TAG_OPTIONS.items():
            field_name = f"{emotion}_tag"
            choices = [('neutral', 'neutral')] + [(tag, tag) for tag in tags]
            self.fields[field_name] = forms.ChoiceField(choices=choices, required=False)