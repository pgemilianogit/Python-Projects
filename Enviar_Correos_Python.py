import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#CREDENCIALES
remitente="emibol.100@gmail.com"
password="dsbw ewac iwmw nojt"

#DETALLES DE DESTINATARIO
destinatario="panfu.100@hotmail.com"
asunto="Prueba de correo"

#CREAR MENSAJE
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = asunto

#CUERPO DEL MENSAJE
cuerpo = "Hola padrino, automatice enviar correo y ando probando"
mensaje.attach(MIMEText( cuerpo, "plain" ))

#INICIAR SESIÓN EN SERVIDOR SMTP DE GMAIL
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login( remitente, password )

#ENVIAR CORREO
texto= mensaje.as_string()
server.sendmail(remitente, destinatario, texto)
server.quit()

print("CORREO ENVIADO")