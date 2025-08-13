from django.urls import path
from . import views

urlpatterns = [
    path('entry/', views.mood_entry, name='mood_entry'),
    path('history/', views.mood_history, name='mood_history'),
]