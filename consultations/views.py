from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from doctors.models import Doctors

from consultations.models import Consultations


def generate_consultation(request):
    if request.method == 'POST':
        consultation_date = request.POST.get('date')
        consultation_user = User.objects.filter(id=request.user.id).first()
        consultation_doctor = Doctors.objects.filter(
            id=request.POST.get('doctor_id')).first()

        consultation = Consultations()

        consultation.consultation_date = consultation_date
        consultation.consultation_user = consultation_user
        consultation.consultation_doctor = consultation_doctor
        consultation.consultation_status = 0
        consultation.save()

        if consultation:
            messages.success(request, 'Doctor creado correctamente')

            return redirect('index')

    else:
        pass
