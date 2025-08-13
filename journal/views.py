from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def journal(request):
    return render(request, 'journal/journal.html')