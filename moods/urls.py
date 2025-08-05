from django.urls import path
from .views import mood_entry

urlpatterns = [
    path('entry/', mood_entry, name='mood_entry'),
]