# Mintic Engrega Spring 4
 Se realiza la Historia de Usuario Proveedor, con las cuatro operaciones POST, GET, UPDATE y DELETE
# requerimientos: Se requiere tener una instancia previa de posgres local o en la nube, la instancia 
no debe haberse utilizado antes.
instale su ambiente virtual y las depencias de sus apuntes de clase (por ejemplo):
pip install virtualenv --user
python -m  venv env
 .\env\Scripts\activate
pip install --upgrade pip
Set-ExecutionPolicy Unrestricted -Scope Process

pip3 install django
pip3 install psycopg2
pip install djangorestframework

Active su ambiente virtual y realize la migracion a su ambiente

.\env\Scripts\activate 
python manage.py makemigrations authApp
python  manage.py  migrate
python .\manage.py runserver
pip3 install psycopg2 

Despliegue de forma local:
 python .\manage.py runserver
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

