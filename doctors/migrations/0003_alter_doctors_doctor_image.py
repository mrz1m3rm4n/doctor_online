# Generated by Django 4.2.5 on 2023-10-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_doctors_doctor_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doctor_image',
            field=models.ImageField(default='images/usuario.png', null=True, upload_to='doctors'),
        ),
    ]
