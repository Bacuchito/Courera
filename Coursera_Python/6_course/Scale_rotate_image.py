#!/usr/bin/env python3
# Importamos las librerías necesarias
from PIL import Image
import os

# Asignamos el directorio de origen y destino de las imágenes
directory = "images/"
output_directory = "/opt/icons/"

# Iniciamos un ciclo para procesar cada imagen en el directorio
for filename in os.listdir(directory):
    # Saltamos el archivo .DS_Store
    if filename != ".DS_Store":
        # Abrimos la imagen y la asignamos a la variable 'im'
        im = Image.open(os.path.join(directory, filename))
        # Giramos la imagen 90 grados en sentido antihorario
        im = im.rotate(-90)
        # Redimensionamos la imagen a 128x128 píxeles
        im = im.resize((128,128))
        # Convertimos la imagen a formato RGB
        im = im.convert("RGB")
        # Guardamos la imagen en el directorio de destino con el mismo nombre y extensión '.jpeg'
        im.save(os.path.join(output_directory, filename+".jpeg"))
