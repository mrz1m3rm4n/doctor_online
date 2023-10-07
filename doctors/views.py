from django.shortcuts import render, redirect
from .models import Doctors
from cities.models import Cities
from specialtys.models import Specialty

from django.contrib.auth.models import User

from storages.backends.s3boto3 import S3Boto3Storage


def doctors_view(request):
    # if request.user.has_perm("perms.doctors.view_doctos"):

    specialtys = Specialty.objects.all()
    cities = Cities.objects.all()

    if request.method == 'POST':
        especialista = request.POST.get('especialista')
        ubicacion = request.POST.get('ubicacion')

        doctors = Doctors.objects.select_related('doctor_id').select_related('doctor_specialty').select_related(
            'doctor_city').filter(doctor_city=ubicacion, doctor_specialty=especialista)

        score = generate_view_doctor(doctors)

        return render(request, 'doctors/index.html', {'doctors': doctors, 'score': score, 'specialtys': specialtys, 'cities': cities})
    else:
        doctors = Doctors.objects.select_related('doctor_id').select_related(
            'doctor_specialty').select_related('doctor_city').all()

        score = generate_view_doctor(doctors)

        return render(request, 'doctors/index.html', {'doctors': doctors, 'score': score, 'specialtys': specialtys, 'cities': cities})
    # else:
    #     return render(request, 'accounts/login.html')


def doctor_view(request, doctor):
    if doctor:
        doctor = Doctors.objects.select_related('doctor_id').select_related(
            'doctor_specialty').select_related('doctor_city').filter(doctor_id=doctor).first()

        parte_entera, parte_decimal = divmod(doctor.doctor_score, 1)

        stars_html = ''.join(['<span class="star star-activate"></span>' if i < parte_entera
                              else '<span class="star star-1-5"></span>' if i == parte_entera and parte_decimal == 0.5
                              else '<span class="star"></span>' for i in range(5)])

        return render(request, 'doctors/doctor_info.html', {'doctor': doctor, 'score': stars_html})
    else:
        return redirect('index')


def generate_view_doctor(data_doctors):
    html_card = []
    for data_doctor in data_doctors:

        parte_entera, parte_decimal = divmod(data_doctor.doctor_score, 1)

        stars_html = ''.join(['<span class="star star-activate"></span>' if i < parte_entera
                              else '<span class="star star-1-5"></span>' if i == parte_entera and parte_decimal == 0.5
                              else '<span class="star"></span>' for i in range(5)])

        card_doctors = f'''
            <div class=" mb-4">
                <div class="col-7">
                    <div class="row">
                        <div class="col-5 card-doctor-img">
                            <img src="{ data_doctor.doctor_image.url }" alt="Logo">

                            <div class="start-container">{stars_html}</div>
                        </div>
                        <div class="col-7 card-doctor">
                            <div>
                                <h2>{ data_doctor.doctor_id.first_name } { data_doctor.doctor_id.last_name }</h2>
                                <p>{ data_doctor.doctor_specialty.specialty_name }</p>
                                <p>Cédula: { data_doctor.doctor_professional_id }</p>
                            </div>
                            <div class="d-flex align-items-center justify-content-between">
                                <p>{ data_doctor.doctor_address }, { data_doctor.doctor_city.city_name }</p>
                                <a class="btn btn-primary" href="doctors/doctor-info/{data_doctor.doctor_id.id}">Buscar</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div  class="col-5"></div>
            </div>
        '''

        html_card.append(card_doctors)

    return html_card
