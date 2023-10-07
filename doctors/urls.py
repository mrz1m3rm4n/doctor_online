from django.urls import path

from .views import doctors_view, doctor_view

urlpatterns = [
    path('', doctors_view, name='doctors'),
    path('doctor-info/<str:doctor>', doctor_view, name='doctor-info'),
]
