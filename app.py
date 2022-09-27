from email import message
from flask import Flask,request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

#Parametros para el funcionamiento del modulo SMTP
app.config['MAIL_SERVER']='smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

#Funcion para definir los parametros para poder enviar correos por medio de dichos parametros
#email: Correo del usuario, pwd: Contraseña del usuario
def setConfig(email,pwd):
    app.config['MAIL_USERNAME'] = email
    app.config['MAIL_PASSWORD'] = pwd
    mail = Mail(app)

#Ruta de prueba 
@app.route("/")
def home():
    return "<h1>Welcome home</h1>"

#Ruta para registrar usuario {No programada}
@app.route("/register")

#Ruta para activar usuaario {No programada}
@app.route("/activate")

#Ruta para inicar sesión {No programada}
@app.route("/login")

#Ruta para recuperar contraseña del usuario {No programada}
@app.route("/recovery")

#Ruta para cambiar contraseña del usuario {No programada}
@app.route("/change")

#Ruta para visualizar los mensaajes del usuario {No programada}
@app.route("/messages")

#Ruta para enviar correos (Temporalmente recibe los parametros por medio Json a traves del metodo POST)
#Utilice para las pruebas Postman o Insomnia
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

