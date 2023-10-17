from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctors


class Reviews(models.Model):
    review_doctor = models.ForeignKey(
        Doctors,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
    )

    review_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
    )

    review_score = models.DecimalField(
        null=True, decimal_places=1, max_digits=10)

    review_description = models.TextField(null=True)

    creted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.review_doctor)
