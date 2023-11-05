Requiere python version 3.11.5 .... versiones en adelante no puede instalar la dependencia de mysqlclient

Creamos entorno virtual

python -m venv env

Activamos entorno virtual

source ./env/Scripts/active

Instalamos los requerimientos

pip install -r ./requerimientos.txt

Ejecutamos el proyecto

python manage.py runserver --settings=settings.local

Creamos el super usuario

python manage.py createsuperuser --settings=settings.local

Se corre las migraciones

python manage.py migrate --settings=settings.local

Se corren este query al intalar la aplicacion

ALTER TABLE `doctors_doctors` CHANGE `doctor_score` `doctor_score` DECIMAL(10,1) NULL DEFAULT '0.0';

INSERT INTO `cities_cities` (`id`, `city_name`, `acreted_date`, `updated_date`) VALUES (NULL, 'CDMX', '', NULL), (NULL, 'Queretaro', '', NULL), (NULL, 'Hidalgo', '', NULL), (NULL, 'Puebla', '', NULL);

INSERT INTO `specialtys_specialty` (`id`, `specialty_name`, `acreted_date`, `updated_date`) VALUES (NULL, 'Medico general', '', NULL), (NULL, 'Psicologo', '', NULL), (NULL, 'Pediatra', '', NULL), (NULL, 'Dentista', '', NULL);
