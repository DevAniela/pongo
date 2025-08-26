from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    
    happy = models.IntegerField(choices=[(i, i) for i in range(1,11)], blank=True, null=True)
    angry = models.IntegerField(choices=[(i, i) for i in range(1,11)], blank=True, null=True)
    sad = models.IntegerField(choices=[(i, i) for i in range(1,11)], blank=True, null=True)
    fear = models.IntegerField(choices=[(i, i) for i in range(1,11)], blank=True, null=True)
    disgust = models.IntegerField(choices=[(i, i) for i in range(1,11)], blank=True, null=True)
    surprise = models.IntegerField(choices=[(i, i) for i in range(1,11)], blank=True, null=True)
    
    happy_tag = models.CharField(max_length=50, blank=True, null=True)
    angry_tag = models.CharField(max_length=50, blank=True, null=True)
    sad_tag = models.CharField(max_length=50, blank=True, null=True)
    fear_tag = models.CharField(max_length=50, blank=True, null=True)
    disgust_tag = models.CharField(max_length=50, blank=True, null=True)
    surprise_tag = models.CharField(max_length=50, blank=True, null=True)
       
    def __str__(self):
        return f"{self.user.username} on {self.timestamp.strftime('%d-%m-%Y')}"