from django.db import models
from django.utils import timezone

from cities.models import Cities
from specialtys.models import Specialty
from django.contrib.auth.models import User


class Doctors(models.Model):
    doctor_phone = models.CharField(null=True, max_length=10)
    doctor_extract = models.CharField(null=True, max_length=150)
    doctor_description = models.TextField(null=True)
    doctor_address = models.TextField(null=True)

    doctor_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='doctors',
        null=True,
    )

    doctor_specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
        related_name='doctors',
        null=True,
    )

    doctor_professional_id = models.CharField(max_length=50)

    doctor_city = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
        related_name="doctors"
    )

    doctor_score = models.DecimalField(
        null=True, decimal_places=1, max_digits=10)

    doctor_image_name = models.CharField(
        max_length=255, null=True, blank=False, default='usuario.png')
    doctor_image = models.ImageField(
        upload_to='doctors', null=True, default='images/usuario.png')

    acreted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.doctor_id)
