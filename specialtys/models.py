from django.db import models


class Specialty(models.Model):
    specialty_name = models.CharField(max_length=20)

    acreted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.specialty_name
