from cities.models import Cities
from django.shortcuts import render
from specialtys.models import Specialty
from doctors.models import Doctors
from doctors.views import generate_view_doctor


def index_view(request):
    if request.user.is_authenticated:
        specialtys = Specialty.objects.all()
        cities = Cities.objects.all()

        doctors = Doctors.objects.select_related('doctor_id').select_related(
            'doctor_specialty').select_related('doctor_city').all()

        score = generate_view_doctor(doctors)

        return render(request, 'doctors/index.html', {'doctors': doctors, 'score': score, 'specialtys': specialtys, 'cities': cities})
    else:
        specialtys = Specialty.objects.all()
        cities = Cities.objects.all()

        return render(request, 'landig_page/index.html', {'specialtys': specialtys, 'cities': cities})
