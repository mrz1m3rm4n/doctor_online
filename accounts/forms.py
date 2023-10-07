from django import forms

from django.contrib.auth.models import User, Group

from cities.models import Cities
from specialtys.models import Specialty
from doctors.models import Doctors


class RegisterForm(forms.Form):
    groups = Group.objects.all()

    first_name = forms.CharField(label='Nombre', required=True, max_length=150)
    last_name = forms.CharField(
        label='Apellidos', required=True, max_length=150)
    email = forms.EmailField(label='Correo electronico', required=True)

    group = forms.ModelChoiceField(
        label='Tipo de usuario', queryset=Group.objects.all(), required=True)

    username = forms.CharField(
        label='Nombre de usuario', required=True, min_length=4, max_length=50)
    password = forms.CharField(
        label='Contraseña', required=True, widget=forms.PasswordInput(attrs={}))
    password2 = forms.CharField(
        label='Confirmar contraseña', required=True, widget=forms.PasswordInput(attrs={}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'El password debe coincidir')

        return cleaned_data

    def save(self):

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        group = self.cleaned_data.get('group')

        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
            **{'first_name': first_name, 'last_name': last_name}
        )

        user.save()

        grupo = Group.objects.get(name=group)
        user.groups.add(grupo)

        return user
