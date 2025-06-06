import requests
from flask import current_app
from os import environ

def get_air(file_name : str = "fileair.csv"):
    # Paso 1: Login para obtener la cookie de sesión
    login_url = "https://ar.air-intra.com/2022/"
    login_data = {
        "urbid": environ.get("URBID"),
        "urbpass": environ.get("URBPASS")
    }

    # Creamos una sesión persistente
    session = requests.Session()
    response = session.post(login_url, data=login_data)

    # Verificamos que obtuvimos la cookie de sesión
    if "PHPSESSID" not in session.cookies.get_dict():
        raise Exception("No se pudo obtener la cookie de sesión (PHPSESSID)")

    # Paso 2: Descarga del archivo CSV usando la sesión activa
    download_url = "https://ar.air-intra.com/consultas/descargas.php?stock=F"
    csv_response = session.get(download_url)

    # Guardar archivo si la respuesta es válida
    if csv_response.status_code == 200 and 'text/csv' in csv_response.headers.get('Content-Type', ''):
        with open(f"/tmp/{file_name}", "wb") as f:
            f.write(csv_response.content)
        print("Archivo descargado correctamente.")
    else:
        print(f"Error al descargar archivo: {csv_response.status_code}")
        print(csv_response.text)
        
    return file_name