# Mintic Engrega Spring 4
 Se realiza la Historia de Usuario Proveedor, con las cuatro operaciones POST, GET, UPDATE y DELETE
# requerimientos: 
Se requiere tener una instancia previa de posgres local o en la nube, la instancia 
no debe haberse utilizado antes, una vez tenga credenciales agregelas en el archivo .setting 


instale su ambiente virtual y las depencias segun sus apuntes de clase ( aqui un ejemplo para windows):
pip install virtualenv --user
python -m  venv env
 .\env\Scripts\activate
pip install --upgrade pip
Set-ExecutionPolicy Unrestricted -Scope Process

pip3 install django
pip3 install psycopg2
pip install djangorestframework
pip3 install psycopg2 

# Active su ambiente virtual y realize la migracion a su instacia de BD

.\env\Scripts\activate 
python manage.py makemigrations manosmaestras
python  manage.py  migrate


# Despliegue de forma local:
Comente las 2 lineas ultimas dos lineas del archivo setting:
'import django_heroku
django_heroku.settings(locals())'

 python .\manage.py runserver
 Ingrese a su navegador: http://localhost:8000
 
POST:
url:              http://localhost:8000/api/v1/proveedor/create/

JSON:


    {
 
        "date_created": "2020-11-19",
        "usuario": "Andersson2321",
        "cedula": "121222",
        "nombre": "Andersson Avila",
        "correo": "andersson@gmail.com",
        "fecha_Nacimiento": "2020-11-19",
        "celular": "12122",
        "años_de_Experiencia": "12",
        "ultimo_Trabajo": "Electricista",
        "costo_Por_Hora": "1000",
        "clave": "1123ws"
    }

GET:             http://localhost:8000/api/v1/proveedor
JSON: No requiere


PUT:             http://localhost:8000/api/v1/proveedor/update/ID/



    {

        "date_created": "2020-11-19",
        "usuario": "Andersson2321",
        "cedula": "121222",
        "nombre": "Andersson ",
        "correo": "andersson@gmail.com",
        "fecha_Nacimiento": "2020-11-19",
        "celular": "12122",
        "años_de_Experiencia": "12",
        "ultimo_Trabajo": "Electricista",
        "costo_Por_Hora": "1000",
        "clave": "1123ws"
    }
DELETE:          http://localhost:8000/api/v1/proveedor/delete/ID/

JSON: No requiere

