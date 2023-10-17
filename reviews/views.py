from django.shortcuts import render, redirect
from .models import Reviews
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from doctors.models import Doctors
from django.db.models import Avg


def create_review(request):
    if request.method == 'POST':

        review_doctor = get_object_or_404(
            Doctors, id=request.POST.get('doctor_id'))
        review_score = request.POST.get('score')
        review_description = request.POST.get('comment')
        review_user = get_object_or_404(User, id=request.user.id)

        try:
            reviews = Reviews.objects.get(
                review_doctor=review_doctor.id, review_user=review_user.id)

            reviews.review_score = review_score
            reviews.review_description = review_description
            reviews.save()

            if reviews:
                update_score_global(review_doctor.id)
                messages.success(
                    request, 'Información actualizada correctamente')
            else:
                messages.error(request, 'Ocurrio un problema al actualizar')

        except Reviews.DoesNotExist:
            reviews = Reviews(
                review_doctor=review_doctor.id,
                review_user=review_user.id,
                review_score=review_score,
                review_description=review_description,
            )

            reviews.save()

            if reviews:
                update_score_global(review_doctor.id)
                messages.success(request, 'Información guardada correctamente')
            else:
                messages.error(request, 'Ocurrio un problema al actualizar')

        return redirect('index')


def update_score_global(doctor):
    review = Reviews.objects.filter(review_doctor=doctor)

    if review.count() > 2:
        promedio = review.aggregate(Avg('review_score'))['review_score__avg']

        decimal_part = promedio - int(promedio)

        if decimal_part < 0.5:
            promedio = str(int(promedio))+".0"
        elif decimal_part >= 0.75:
            promedio = int(promedio)+1
        else:
            promedio = int(promedio)+0.5

        doctor = Doctors.objects.get(id=doctor)
        doctor.doctor_score = promedio
        doctor.save()
    else:
        doctor = Doctors.objects.get(id=doctor)
        doctor.doctor_score = review.first().review_score
        doctor.save()
