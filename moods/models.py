from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.IntegerField(choices=[(i, i) for i in range(1,11)])
    emotion_tags = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.mood} on {self.timestamp.strftime('%d-%m-%Y')}"