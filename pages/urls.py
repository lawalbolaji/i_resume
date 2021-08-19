from .views import resumeView
from django.urls import path



urlpatterns = [
    path('', resumeView, name = 'resume'),
]