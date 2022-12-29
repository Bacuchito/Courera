#!/usr/bin/env python3

# Importamos las librerías shutil, psutil, socket y emails
import shutil
import psutil
import socket
import emails
import os

# Definimos la dirección del remitente y del destinatario del correo
sender = "automation@example.com"
# El destinatario será el nombre de usuario actual del sistema
receiver = "<USERNAME>@example.com".format(os.environ.get('USER'))
# Definimos el cuerpo del mensaje
body = "Please check your system and resolve the issue as soon as possible."

# Comprobamos el espacio disponible en el disco y enviamos un correo si es < 20%
du = shutil.disk_usage("/")
du_prsnt = du.free/du.total * 100
if du_prsnt < 20:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Comprobamos el uso de la CPU y enviamos un correo si es >80%
cpu_prsnt = psutil.cpu_percent(1)
if cpu_prsnt > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Comprobamos la memoria disponible, si es < 500mb enviamos un correo
mem = psutil.virtual_memory()
trs = 500 * 1024 * 1024  # 500MB
if mem.available < trs:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

# Comprobamos el nombre del host y si no puede resolverse a "127.0.0.1" enviamos un correo
hostname = socket.gethostbyname('localhost')
if hostname != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

