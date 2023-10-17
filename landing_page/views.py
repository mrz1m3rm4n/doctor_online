from cities.models import Cities
from django.shortcuts import render, redirect
from specialtys.models import Specialty
from doctors.models import Doctors
from doctors.views import generate_view_doctor


def index_view(request):
    if request.user.is_authenticated:
        return redirect('doctors')
    else:
        specialtys = Specialty.objects.all()
        cities = Cities.objects.all()

        return render(request, 'landig_page/index.html', {'specialtys': specialtys, 'cities': cities})
