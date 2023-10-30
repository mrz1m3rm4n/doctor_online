from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm
from cities.models import Cities
from doctors.models import Doctors
from specialtys.models import Specialty

from django.contrib.auth.decorators import (
    login_required, permission_required)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('do_username')
        password = request.POST.get('do_password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(
                request, 'Usuario logeado {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()

        if user:
            login(request, user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('index')
        else:
            messages.error(request, 'Error en el registro')
            return redirect('register')
    else:
        group = Group.objects.all()

        return render(request, 'accounts/register.html', {'form': form, 'group': group})


@login_required
# @permission_required('accounts.change_doctors', raise_exception=True)
def profile_view(request):
    try:
        data_profile = Doctors.objects.get(doctor_id=request.user.id)
    except ObjectDoesNotExist:
        data_profile = None

    if request.method == 'POST' and request.FILES.get('imagen'):

        doctor_image = request.FILES['imagen']
        doctor_image_name = request.FILES['imagen'].name

        phone = request.POST.get('phone')
        description = request.POST.get('description')
        extract = request.POST.get('extract')
        address = request.POST.get('address')
        doctor_professional_id = request.POST.get('doctor_professional_id')
        city_id = request.POST.get('city')
        specialty_id = request.POST.get('specialty')

        user = request.user  # Obtén la instancia completa del usuario actual

        try:
            doctor = Doctors.objects.get(doctor_id=user)

            doctor.doctor_phone = phone
            doctor.doctor_description = description
            doctor.doctor_extract = extract
            doctor.doctor_address = address
            doctor.doctor_professional_id = doctor_professional_id
            doctor.doctor_city_id = city_id
            doctor.doctor_image = doctor_image
            doctor.doctor_image_name = doctor_image_name
            doctor.doctor_specialty_id = specialty_id
            doctor.save()

            messages.success(
                request, 'Información actualizada correctamente')
        except Doctors.DoesNotExist:
            doctor = Doctors(
                doctor_id=user,
                doctor_phone=phone,
                doctor_description=description,
                doctor_extract=extract,
                doctor_address=address,
                doctor_professional_id=doctor_professional_id,
                doctor_city_id=city_id,
                doctor_image=doctor_image,
                doctor_score=0.0,
                doctor_image_name=doctor_image_name,
                doctor_specialty_id=specialty_id,
            )
            doctor.save()

            messages.success(request, 'Doctor creado correctamente')

        return redirect('profile')
    else:
        cities = Cities.objects.all()
        specialtys = Specialty.objects.all()

        return render(request, 'accounts/profile.html', {'user_data': data_profile, 'cities': cities, 'specialtys': specialtys})
