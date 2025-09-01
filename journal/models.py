from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    
    def __str__(self):
        return f"Entry by {self.user.username} on {self.timestamp.strftime('%d-%m-%Y %H:%M')}"