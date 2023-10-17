from django.urls import path

from .views import create_review

urlpatterns = [
    path('save', create_review, name='save'),
]
