# credito
instrucciones de uso
antes de esto debes tener una base de datos en postgres que se llame "credito"
y si tienes una contraseña diferente de "password" modifcar el archivo
![image](https://user-images.githubusercontent.com/56244689/125176109-85bc8280-e196-11eb-94a2-a5ed207d7c6f.png)
1. descarga o clona el proyecto
2. ejecuta python -m venv env
3. "cd env/scripts"
4. ejecuta "activate"
5. cd ../../src
6. pip install django
7. pip install django-environ
8. pip install django-allauth
9. pip install django-crispy-forms
10. pip install psycopg2
11. pip install pillow
12. ejecuta "python manage.py makemigrations"
13. ejecuta "python manage.py migrate"

(para lo siguiente necesitas un superuser entonces ejecuta "python manage.py createsuperuser" y sigue los pasos)

15. ejecuta python manage.py runserver
16. ingresa a localhost:8000
