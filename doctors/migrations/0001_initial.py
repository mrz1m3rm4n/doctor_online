# Generated by Django 4.2.5 on 2023-09-29 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cities', '0001_initial'),
        ('specialtys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_phone', models.CharField(max_length=10, null=True)),
                ('doctor_description', models.TextField(null=True)),
                ('doctor_address', models.TextField(null=True)),
                ('doctor_professional_id', models.CharField(max_length=50)),
                ('doctor_score', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('doctor_image_name', models.CharField(max_length=255)),
                ('doctor_image', models.ImageField(upload_to='images')),
                ('acreted_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField()),
                ('doctor_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='cities.cities')),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to=settings.AUTH_USER_MODEL)),
                ('doctor_specialty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='specialtys.specialty')),
            ],
        ),
    ]
