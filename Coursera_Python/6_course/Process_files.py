#!/usr/bin/env python3
# Importamos las librerías necesarias
import os
import requests

# Asignamos el directorio de origen de los archivos de feedback
src_dir = "/data/feedback/"

# Capturamos la lista de archivos en el directorio
files = os.listdir(src_dir)

# Definimos una función para leer las líneas de un archivo en una lista
def readlines(file):
    with open(src_dir + file) as f:
        lines = f.read().splitlines()
    return lines

# Creamos una lista vacía para almacenar los diccionarios de feedback
feedback = []

# Asignamos una lista de claves para cada diccionario
keys = ["title", "name", "date", "feedback"]

# Iniciamos un ciclo para procesar cada archivo
for file in files:
    # Leemos las líneas del archivo en una lista
    lines = readlines(file)
    # Creamos un diccionario a partir de las líneas y las claves
    feedback_dict = dict(zip(keys, lines))
    # Agregamos el diccionario a la lista 'feedback'
    feedback.append(feedback_dict)

# Asignamos la URL del servidor de destino
url = "http://localhost/feedback/"

# Iniciamos un ciclo para enviar cada entrada de feedback al servidor
for entry in feedback:
    # Enviamos la entrada al servidor y asignamos la respuesta a la variable 'response'
    response = requests.post(url, data=entry)
    # Si la respuesta es correcta, imprimimos un mensaje
    if response.ok:
        print("loaded entry")
    # Si la respuesta es incorrecta, imprimimos un mensaje con el código de estado de la respuesta
    else:
        print(f"load entry error: {response.status_code}")
