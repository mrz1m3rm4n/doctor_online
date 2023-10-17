from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('landing_page.urls')),
    path('doctors/', include('doctors.urls')),
    path('accounts/', include('accounts.urls')),
    path('consultations/', include('consultations.urls')),
    path('reviews/', include('reviews.urls')),
    path('admin/', admin.site.urls),
]
