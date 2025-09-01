from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import JournalEntryForm
from .forms import JournalEntry

@login_required
def journal_view(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('journal')
    else:
        form = JournalEntryForm()
        
    entries = JournalEntry.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'journal/journal.html', {'form': form, 'entries': entries})