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
    happy_tag = forms.ChoiceField(choices=[('neutral', 'neutral')] + [(tag, tag) for tag in EMOTION_TAG_OPTIONS['happy']], required=False)
    angry_tag = forms.ChoiceField(choices=[('neutral', 'neutral')] + [(tag, tag) for tag in EMOTION_TAG_OPTIONS['angry']], required=False)
    sad_tag = forms.ChoiceField(choices=[('neutral', 'neutral')] + [(tag, tag) for tag in EMOTION_TAG_OPTIONS['sad']], required=False)
    fear_tag = forms.ChoiceField(choices=[('neutral', 'neutral')] + [(tag, tag) for tag in EMOTION_TAG_OPTIONS['fear']], required=False)
    disgust_tag = forms.ChoiceField(choices=[('neutral', 'neutral')] + [(tag, tag) for tag in EMOTION_TAG_OPTIONS['disgust']], required=False)
    surprise_tag = forms.ChoiceField(choices=[('neutral', 'neutral')] + [(tag, tag) for tag in EMOTION_TAG_OPTIONS['surprise']], required=False)
    
    class Meta:
        model = MoodEntry
        fields = ['happy', 'happy_tag', 'angry', 'angry_tag', 'sad', 'sad_tag', 'fear', 'fear_tag', 'disgust', 'disgust_tag', 'surprise', 'surprise_tag']