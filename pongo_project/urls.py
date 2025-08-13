from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('moods/', include('moods.urls')),
    path('/journal', include('journal.urls')),
    path('/chat', include('chat.urls')),
]
