from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MoodEntryForm

@login_required
def mood_entry(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            return redirect('mood_history')
    else:
        form = MoodEntryForm()
    return render(request, 'moods/mood_entry.html', {'form': form})

@login_required
def mood_history(request):
    moods = request.user.moodentry_set.all().order_by('-timestamp')
    return render(request, 'moods/mood_history.html', { 'moods': moods })