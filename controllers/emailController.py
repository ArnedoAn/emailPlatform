from flask import Flask
from flask_mail import Mail, Message
from controllers.dbController import getSenderParams

app = Flask(__name__)
mail = Mail(app)

params = getSenderParams('4nDr3z.uninorte')
email = str(params[0])
pwd = str(params[1])
print(email, pwd)
# Parametros para el funcionamiento del modulo SMTP
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = pwd

mail = Mail(app)




# def setParams():
    
#     if(params!=False):
#         setConfig(str(params[0]),str(params[1]))
#     else:
#         print("ERROR DE PARAMETROS DE SMTP")    

def sendActivation(emailTo, cod):
    #setParams()
    host = "http://127.0.0.1:5000"
    link = host + f"/activate?email={emailTo}&cod={cod}"
    try:
        msg = Message('ACTIVA TU CUENTA!', sender=email, recipients=[emailTo])
        msg.body = f"Activa tu cuenta mediante este enlace {link}"
        mail.send(msg)
        return True
    except Exception as ex:
        print(ex)
        return False


def sendReset(emailTo):
    #setParams()
    host = "http://127.0.0.1:5000"
    link = host + f"/change?email={emailTo}"
    try:
        msg = Message('CAMBIO DE CONTRASEÑA', sender=email, recipients=[emailTo])
        msg.body = f"Cambia tu contraseña mediante este link {link}"
        mail.send(msg)
        return True
    except Exception as ex:
        print(ex)
        return False