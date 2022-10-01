from flask import Blueprint, request, Flask
from flask_mail import Mail, Message
from controllers.dbController import getSenderParams

app = Flask(__name__)

send = Blueprint('send', __name__, template_folder='templates')

mail = Mail(app)

# Parametros para el funcionamiento del modulo SMTP
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


def setConfig(email, pwd):
    app.config['MAIL_USERNAME'] = email
    app.config['MAIL_PASSWORD'] = pwd
    mail = Mail(app)


params = getSenderParams('12345')
if(params!=False):  
    email = params.email
    setConfig(params.email,params.password)
else:
    print("ERROR DE PARAMETROS DE SMTP")    


@send.route("/send", methods=['POST'])
def sendEmail():
    try:
        jsonData = request.get_json()
        message = str(jsonData['message'])
        emailTo = str(jsonData['to'])
        msg = Message('TIENES UN MENSAJE!', sender=email, recipients=[emailTo])
        msg.body = f"El mensaje enviado por {email} es: {message}"
        mail.send(msg)
        return "<h1>Enviado!</h1>"
    except Exception as ex:
        print(ex)
        return "<h1>Error!</h1>"


def sendActivation(emailTo, cod):
    host = "http://127.0.0.1:5000"
    link = host + f"/activate?email={email}&cod={cod}"
    try:
        msg = Message('ACTIVA TU CUENTA!', sender=email, recipients=[emailTo])
        msg.body = f"Activa tu cuenta mediante este enlace {link}"
        mail.send(msg)
        return True
    except Exception as ex:
        print(ex)
        return False
