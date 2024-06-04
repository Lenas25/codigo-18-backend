from email.mime.multipart import MIMEMultipart
# protocolo de mensajes de internet
from smtplib import SMTP
from email.mime.text import MIMEText
# otra librería para encriptar
from cryptography.fernet import Fernet
from os import environ
from dotenv import load_dotenv

load_dotenv()

def olvide_password(destinatario):
    print('Enviando correo a {}'.format(destinatario))
    fernet = Fernet(environ.get('FERNET_KEY'))

    token = fernet.encrypt(bytes(destinatario, 'utf-8'))

    email = environ.get('EMAIL_EMISOR')
    password = environ.get('PASSWORD_EMAIL_EMISOR')

    #Titulo del correo
    mensaje = MIMEMultipart()
    mensaje['Subject'] = 'Olvidaste tu contraseña'
    mensaje['From'] = email
    mensaje['To'] = destinatario
    
    cuerpo = "Parece que has olvidado tu contraseña, por favor sigue el siguiente enlace para recuperarla -> http://localhost:5000/cambiar-password?token={}".format(token.decode('utf-8'))
    text = MIMEText(cuerpo)
    mensaje.attach(text)
    #                         SERVIDOR       | PUERTO
    # outlook   outlook.office365.com       | 587
    # gmail     smtp.gmail.com             | 587
    # hotmail   smtp.live.com             | 587
    # yahoo     smtp.mail.yahoo.com      | 587
    # icloud    smtp.mail.me.com        | 587
    emisor = SMTP('smtp.gmail.com', 587)

    # empezar la comunicación con el servidor
    emisor.starttls()

    # emisor.login(email, password)
    try:
        emisor.login(email, password)
        emisor.sendmail(email, destinatario, mensaje.as_string())
        print('Correo enviado correctamente')
    except Exception as e:
        print('Error al enviar el correo')
        print(e)

    # cerrar la conexión con el servidor
    emisor.quit()
