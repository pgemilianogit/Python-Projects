import smtplib                                      #LIBERIA DE ENVIOS
from email.mime.text import MIMEText                #Permite ajustar texto plano o archivos html
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase
from email import encoders                          #Enviar archivo adjunto
import os

def enviar_correo(remitente, password, destinatarios, asunto, cuerpo, archivo_adjunto=None):
    
    #CREAR MENSAJE A ENVIAR
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto

    #Adjuntar partes del correo, adjuntar componentes del correo y el contructor crea una instancia que representa el mesaje
    #varieble que contiene el desarrollo, indicando que el tipo de texto es plano, sin formato especial, negita, cursiva, etc.
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # ADJUNTAR ARCHIVO
    if archivo_adjunto:
        nombre_archivo = os.path.basename(archivo_adjunto)
        parte = MIMEBase('application', "octet-stream")
        with open(archivo_adjunto, 'rb') as archivo:
            parte.set_payload(archivo.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={nombre_archivo}')
        mensaje.attach(parte)

#INICIAR SESIÓN EN SERVIDOR SMTP DE GMAIL    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(remitente, password)
    texto = mensaje.as_string()
    server.sendmail(remitente, destinatarios, texto)

    # sALIR DE LA SESIÓN SMTP
    server.quit()

#DEFINIR CREDENCIALES (Generar contraseña de aplicaciones)
remitente = "emibol.100@gmail.com"
password = "dsbw ewac iwmw nojt"

#DETALLES DE DESTINATARIOS
destinatarios = ["panfu.100@hotmail.com", "pgemiliano@hotmail.com"]         #USUARIOS
asunto = "Prueba de correo"
cuerpo = "Hola, pruebas de enviar correo por Python con una imagen adjunta."

# AGREGAR ARCHIVO ADJUNTO LOCAL (opcional)
archivo_adjunto = "C:/Users/panfu/Music/Proyectos/Imagenes de Pruebas/1.jpg"  #RUTA DE ARCHIVO LOCAL

# ENVIAR CORREO
enviar_correo(remitente, password, destinatarios, asunto, cuerpo, archivo_adjunto)
print("CORREO ENVIADO A LOS DESTINATARIOS:", destinatarios)