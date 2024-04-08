import smtplib                                      #LIBERIA DE ENVIOS
from email.mime.text import MIMEText                #Permite ajustar texto plano o archivos html
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase
from email import encoders                          #Enviar archivo adjunto
import os

#Generar contraseñas de aplicaciones

#DEFINIR CREDENCIALES
remitente="emibol.100@gmail.com"
password="dsbw ewac iwmw nojt"

#DETALLES DE DESTINATARIO
destinatario="armandoxicoc12@gmail.com"
asunto="Prueba de correo"

#CREAR MENSAJE A ENVIAR 
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = asunto

#CUERPO DEL MENSAJE
cuerpo = "Hola, pruebas de enviar correo por Python con una imagen adjunta."
#Adjuntar partes del correo, adjuntar componentes del correo y el contructor crea una instancia que representa el mesaje
#varieble que contiene el desarrollo, indicando que el tipo de texto es plano, sin formato especial, negita, cursiva, etc.
mensaje.attach(MIMEText( cuerpo, "plain" ))


# AGREGAR ARCHIVO ADJUNTO LOCAL
archivo_adjunto_path = "C:/Users/panfu/Music/Proyectos/Imagenes de Pruebas/1.jpg"  # Asegúrate de cambiar esto por la ruta real del archivo
nombre_archivo = os.path.basename(archivo_adjunto_path)
parte = MIMEBase('application', "octet-stream")
with open(archivo_adjunto_path, 'rb') as archivo:
    parte.set_payload(archivo.read())
encoders.encode_base64(parte)
parte.add_header('Content-Disposition', f'attachment; filename={nombre_archivo}')
mensaje.attach(parte)

#INICIAR SESIÓN EN SERVIDOR SMTP DE GMAIL
server = smtplib.SMTP("smtp.gmail.com",587)         #Libreria con la direccion y el puerto
server.starttls()                                   #Iniciar el servidor
server.login( remitente, password )                 #Loguear 

#ENVIAR CORREO
texto= mensaje.as_string()                          #Todo a string
server.sendmail(remitente, destinatario, texto)     #Enviar el correo transfiendo destino
server.quit()

print("CORREO ENVIADO")