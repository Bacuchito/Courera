#!/usr/bin/env python3

# Importamos la librería Image de la librería PIL (Python Imaging Library)
# y la librería os
from PIL import Image
import os

# Definimos la ruta de acceso al directorio de imágenes
path = "./supplier-data/images/"

# Recorremos todos los archivos del directorio
for f in os.listdir("./supplier-data/images"):
    # Filtrar solo los archivos que tengan la extensión .tiff
    if f.endswith(".tiff"):
        # Dividir el nombre del archivo por el carácter . y guardar en split_f
        split_f = f.split(".")
        # Definir el nombre del archivo resultante
        name = split_f[0] + ".jpeg"
        # Abrir el archivo y convertirlo a formato RGB
        im = Image.open(path + f).convert("RGB")
        # Redimensionar la imagen a 600x400 píxeles y guardar en el mismo directorio
        im.resize((600, 400)).save("./supplier-data/images/" + name, "JPEG")

