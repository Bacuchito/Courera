#!/usr/bin/env python3

# Importamos la librería requests y os
import requests
import os

# Esta es la URL del servidor donde se subirá el archivo
url = "http://localhost/upload/"

# Recorremos todos los archivos del directorio
for f in os.listdir("./supplier-data/images"):
    # Filtrar solo los archivos que tengan la extensión .jpeg
    if f.endswith(".jpeg"):
        # Abrir el archivo en modo binario y guardarlo en la variable opened
        with open('./supplier-data/images/' + f, 'rb') as opened:
            # Utilizamos la función post() de la librería requests para enviar el archivo
            # al servidor especificado en la URL. La función files permite enviar el archivo
            # como parte de la petición HTTP POST
            r = requests.post(url, files={'file': opened})
