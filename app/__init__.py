from flask import Flask, request
from flask_mail import Mail, Message
from app.views.send import send
from app.views.login import login
from app.views.register import register
from app.views.activate import activate
from app.views.reset import reset
from app.views.messages import messages
from app.controllers.dbController import getSenderParams, registerUser
from app.controllers.pwdController import makePwd
import secrets

app = Flask(__name__)
app.secret_key="TEMPORAL"

app.register_blueprint(send)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(activate)
app.register_blueprint(reset)
app.register_blueprint(messages)

params = getSenderParams('4nDr3z.uninorte')
if(params != False):
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = str(params[0])
    app.config['MAIL_PASSWORD'] = str(params[1])
    app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
else:
    print("Error credenciales de correo")

mail = Mail(app)


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
        msg = Message('CAMBIO DE CONTRASEÑA',
                      sender=email, recipients=[emailTo])
        msg.body = f"Cambia tu contraseña mediante este link {link}"
        mail.send(msg)
        return True
    except Exception as ex:
        print(ex)
        return False


@app.route("/")
def home():
    return "<h1>Welcome home</h1>"


@app.route('/register', methods=["POST"])
def register_User():
    if request.method == "POST":
        data = {}
        jsond = request.get_json()
        data['email'] = str(jsond["email"])
        data['username'] = str(jsond["username"])
        pwd = str(jsond['password'])
        # data['email'] = request.form['email']
        # data['username'] = request.form['name']
        data['token'] = secrets.token_urlsafe()
        # pwd = request.form['pwd']
        data['password'] = makePwd(pwd)
        if(registerUser(data)):
            if(sendActivation(data['email'], data['token'])):
                return 'Link de activación enviado!'
            else:
                return "Error al enviar link de activación"
        else:
            return 'Template de mal registro'


@app.route('/reset', methods=["POST"])
def sendToChange():
    if request.method == "POST":
        email = request.form["email"]
        if(sendReset(email)):
            return "Correo de recuperacion enviado"
        else:
            return "Error al enviar correo de recuperacion"
