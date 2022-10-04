from flask_mail import Message, Mail
from flask import Flask, current_app

app = Flask(__name__)

with app.app_context():
    mail = Mail(current_app)

def sendActivation(emailTo, cod):
    host = "http://127.0.0.1:5000"
    link = host + f"/activate?email={emailTo}&cod={cod}"
    email = "aarnedoe@uninorte.edu.co"
    try:
        msg = Message('ACTIVA TU CUENTA!', sender=email, recipients=[emailTo])
        msg.body = f"Activa tu cuenta mediante este enlace {link}"
        mail.send(msg)
        return True
    except Exception as ex:
        print(ex)
        return False


def sendReset(emailTo):
    host = "http://127.0.0.1:5000"
    link = host + f"/change?email={emailTo}"
    email = "aarnedoe@uninorte.edu.co"
    try:
        msg = Message('CAMBIO DE CONTRASEÑA', sender=email, recipients=[emailTo])
        msg.body = f"Cambia tu contraseña mediante este link {link}"
        mail.send(msg)
        return True
    except Exception as ex:
        print(ex)
        return False
