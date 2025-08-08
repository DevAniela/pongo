from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    
    happy = models.IntegerField(choices=[(i, i) for i in range(1,11)])
    angry = models.IntegerField(choices=[(i, i) for i in range(1,11)])
    sad = models.IntegerField(choices=[(i, i) for i in range(1,11)])
    fear = models.IntegerField(choices=[(i, i) for i in range(1,11)])
    disgust = models.IntegerField(choices=[(i, i) for i in range(1,11)])
    surprise = models.IntegerField(choices=[(i, i) for i in range(1,11)])
    
    happy_tag = models.CharField(max_length=50, default='neutral')
    angry_tag = models.CharField(max_length=50, default='neutral')
    sad_tag = models.CharField(max_length=50, default='neutral')
    fear_tag = models.CharField(max_length=50, default='neutral')
    disgust_tag = models.CharField(max_length=50, default='neutral')
    surprise_tag = models.CharField(max_length=50, default='neutral')
       
    def __str__(self):
        return f"{self.user.username} on {self.timestamp.strftime('%d-%m-%Y')}"