from django.urls import path

from .views import generate_consultation, get_consultation

urlpatterns = [
    path('', generate_consultation, name='consultation'),
    path('my-consultation', get_consultation, name='my-consultation'),
]
