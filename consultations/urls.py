from django.urls import path

from .views import generate_consultation

urlpatterns = [
    path('', generate_consultation, name='consultation'),
]
