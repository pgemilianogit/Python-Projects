import smtplib                                      #LIBERIA DE ENVIOS
from email.mime.text import MIMEText                #Permite ajustar texto plano o archivos html
from email.mime.multipart import MIMEMultipart  

#Generar contraseñas de aplicaciones

#DEFINIR CREDENCIALES
remitente="emibol.100@gmail.com"
password="dsbw ewac iwmw nojt"

#DETALLES DE DESTINATARIO
destinatario="panfu.100@hotmail.com"
asunto="Prueba de correo"

#CREAR MENSAJE A ENVIAR 
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = asunto

#CUERPO DEL MENSAJE
cuerpo = "Hola pruebas de enviar correo por python"
#Adjuntar partes del correo, adjuntar componentes del correo y el contructor crea una instancia que representa el mesaje
#varieble que contiene el desarrollo, indicando que el tipo de texto es plano, sin formato especial, negita, cursiva, etc.
mensaje.attach(MIMEText( cuerpo, "plain" ))


#INICIAR SESIÓN EN SERVIDOR SMTP DE GMAIL
server = smtplib.SMTP("smtp.gmail.com",587)         #Libreria con la direccion y el puerto
server.starttls()                                   #Iniciar el servidor
server.login( remitente, password )                 #Loguear 

#ENVIAR CORREO
texto= mensaje.as_string()                          #Todo a string
server.sendmail(remitente, destinatario, texto)     #Enviar el correo transfiendo destino
server.quit()

print("CORREO ENVIADO")