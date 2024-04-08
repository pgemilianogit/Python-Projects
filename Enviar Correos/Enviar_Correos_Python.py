import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import time, datetime, timedelta

def enviar_correo(remitente, password, destinatarios, asunto, cuerpo, archivo_adjunto=None, hora_programada=None):
    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto

    # Adjuntar cuerpo del mensaje
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar archivo adjunto si se proporciona
    if archivo_adjunto:
        nombre_archivo = os.path.basename(archivo_adjunto)
        parte = MIMEBase('application', "octet-stream")
        with open(archivo_adjunto, 'rb') as archivo:
            parte.set_payload(archivo.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={nombre_archivo}')
        mensaje.attach(parte)
        
    # Si se proporciona la hora programada, calcular el tiempo de espera
    if hora_programada:
        # Calcular la diferencia de tiempo entre ahora y la hora programada
        hora_programada_datetime = datetime.combine(datetime.now().date(), hora_programada)
        if hora_programada_datetime < datetime.now():
            # Si la hora programada ya ha pasado para hoy, programar para mañana
            hora_programada_datetime += timedelta(days=1)
        tiempo_espera = hora_programada_datetime - datetime.now()

        # Esperar hasta la hora programada para enviar el correo
        if tiempo_espera.total_seconds() > 0:
            print(f"Esperando {tiempo_espera} para enviar el correo...")
            import time
            time.sleep(tiempo_espera.total_seconds())
            
    # Iniciar sesión en el servidor SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(remitente, password)
    
    # Enviar correo a cada destinatario
    texto = mensaje.as_string()
    server.sendmail(remitente, destinatarios, texto)

    # Salir de la sesión SMTP
    server.quit()

# DEFINIR CREDENCIALES (Generar contraseña de aplicaciones)
remitente = "emibol.100@gmail.com"
password = "dsbw ewac iwmw nojt"

# DETALLES DE DESTINATARIOS
destinatarios = ["panfu.100@hotmail.com", "pgemiliano@hotmail.com"]  # USUARIOS
asunto = "Prueba de correo"
cuerpo = "Hola, pruebas de enviar correo por Python con una imagen adjunta."

# AGREGAR ARCHIVO ADJUNTO LOCAL (opcional)
archivo_adjunto = "C:/Users/panfu/Music/Proyectos/Imagenes de Pruebas/1.jpg"  # RUTA DE ARCHIVO LOCAL

# PROGRAMAR EL ENVÍO Hora, Minutos
hora_programada = time(15, 55)

# ENVIAR CORREO
enviar_correo(remitente, password, destinatarios, asunto, cuerpo, archivo_adjunto, hora_programada)
print("CORREO ENVIADO A LOS DESTINATARIOS:", destinatarios)
