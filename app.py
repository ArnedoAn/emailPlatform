from email import message
from flask import Flask,request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

def setConfig(email,pwd):
    app.config['MAIL_USERNAME'] = email
    app.config['MAIL_PASSWORD'] = pwd
    mail = Mail(app)

@app.route("/")
def home():
    return "<h1>Welcome home</h1>"

@app.post("/send")
def sendMail():
    try:
        jsonData = request.get_json()
        email = str(jsonData['email'])
        password = str(jsonData['password'])
        message = str(jsonData['message'])
        emailTo = str(jsonData['to'])
        setConfig(email,password)
        msg = Message('TIENES UN MENSAJE!', sender=email, recipients=[emailTo])
        msg.body=f"El mensaje enviado por {email} es: {message}"
        mail.send(msg)
        return "<h1>Enviado!</h1>"
    except:
        return "<h1>Error!</h1>"

