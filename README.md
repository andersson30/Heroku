# Mintic Engrega Spring 4
 Se realiza la Historia de Usuario Proveedor, con las cuatro operaciones POST, GET, UPDATE y DELETE




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

