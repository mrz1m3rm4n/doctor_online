from django.db import models

from doctors.models import Doctors

from django.contrib.auth.models import User


class Consultations(models.Model):
    consultation_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='consultations',
        null=True,
    )

    consultation_doctor = models.ForeignKey(
        Doctors,
        on_delete=models.CASCADE,
        related_name='consultations',
        null=True,
    )

    consultation_status = models.IntegerField(null=False, default=0)

    consultation_date = models.DateTimeField(null=True)
    consultation_descriptionm = models.TextField(null=True)

    acreted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.consultation_user)
