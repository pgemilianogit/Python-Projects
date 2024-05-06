import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import time, datetime, timedelta



def enviar_correo(remitente, password, destinatarios, asunto, cuerpo, archivo_adjunto=None, hora_programada=None):
    
    #CREAR EL MENSAJE
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto

    # ARCHIVO DEL CUERPO DEL MENSAJE
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # ARCHIVO ADJUNTO
    if archivo_adjunto:
        nombre_archivo = os.path.basename(archivo_adjunto)
        parte = MIMEBase('application', "octet-stream")
        with open(archivo_adjunto, 'rb') as archivo:
            parte.set_payload(archivo.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={nombre_archivo}')
        mensaje.attach(parte)
        
    #PROGRAMACION DE LA HORA
    if hora_programada:
        #CALCULAR EL TIEMPO DE HORA PROGRAMADA Y LA ACTUAL
        hora_programada_datetime = datetime.combine(datetime.now().date(), hora_programada)
        if hora_programada_datetime < datetime.now():
            
            #SI LA HORA PROGRAMADA YA PASO, SE ENVIARA AL OTRO DIA
            hora_programada_datetime += timedelta(days=1)
        tiempo_espera = hora_programada_datetime - datetime.now()

        #ESPERA DE LA HORA PARA ENVIAR CORREO
        if tiempo_espera.total_seconds() > 0:
            print(f"Esperando {tiempo_espera} para enviar el correo...")
            import time
            time.sleep(tiempo_espera.total_seconds())
            
    # Iniciar sesión en el servidor SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(remitente, password)
    
    #SOLO TIPO DE TEXTO STRING
    texto = mensaje.as_string()
    server.sendmail(remitente, destinatarios, texto)

    # SALIR DE SMTP
    server.quit()

# DEFINIR CREDENCIALES (Generar contraseña de aplicaciones)
remitente = "emibol.100@gmail.com"
password = "dsbw ewac iwmw nojt"

# DETALLES DE DESTINATARIOS
destinatarios = ["panfu.100@hotmail.com", "pgemiliano@hotmail.com"]  # USUARIOS
asunto = "Prueba de correos"
cuerpo = "Hola, pruebas de enviar correo por Python con una imagen adjunta."

# AGREGAR ARCHIVO ADJUNTO LOCAL (opcional)
archivo_adjunto = "C:/Users/panfu/Music/Proyectos/Imagenes de Pruebas/1.jpg"  # RUTA DE ARCHIVO LOCAL

# PROGRAMAR EL ENVÍO Hora, Minutos
hora_programada = time(15, 55)

# ENVIAR CORREO
enviar_correo(remitente, password, destinatarios, asunto, cuerpo, archivo_adjunto, hora_programada)
print("CORREO ENVIADO A LOS DESTINATARIOS:", destinatarios)
