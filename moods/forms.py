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
        fields = ['happy', 'angry', 'sad', 'fear', 'disgust', 'surprise',
                  'happy_tag', 'angry_tag', 'sad_tag', 'fear_tag', 'disgust_tag', 'surprise_tag']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for emotion in EMOTION_TAG_OPTIONS.keys():
            self.fields[emotion].required = False
            self.fields[emotion].widget.attrs.update({'class': 'form-select'})
        
        for emotion, tags in EMOTION_TAG_OPTIONS.items():
            field_name = f"{emotion}_tag"
            choices = [('', '---')] + [(tag, tag) for tag in tags]
            self.fields[field_name] = forms.ChoiceField(
                choices=choices,
                required=False,
                widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
            )
    
    def grouped_fields(self):
        groups = []
        for emotion in EMOTION_TAG_OPTIONS.keys():
            groups.append((self[emotion], self[f"{emotion}_tag"]))
        return groups