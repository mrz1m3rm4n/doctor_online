from django.contrib import admin
from .models import Doctors, Specialty, Cities

admin.site.register(Doctors)
admin.site.register(Specialty)
admin.site.register(Cities)
