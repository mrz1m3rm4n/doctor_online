Creamos entorno virtual

python -m venv env

Activamos entorno virtual

source ./env/Scripts/active

Installar django

pip install django

Instalamos los requerimientos

pip install -r ./requerimientos.txt

Ejecutamos el proyecto

python manage.py runserver --settings=settings.local

Creamos el super usuario

python manage.py createsuperuser --settings=settings.local
