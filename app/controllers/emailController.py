from flask_mail import Message, Mail
from flask import current_app, Flask
from app.controllers.dbController import getSenderParams

# app = Flask(__name__)
# appx = app.app_context()

# with app.app_context():
#     params = getSenderParams('4nDr3z.uninorte')
#     if(params!=False):
#         app.config['MAIL_PORT'] = 587
#         app.config['MAIL_USE_TLS'] = True
#         app.config['MAIL_USE_SSL'] = False
#         app.config['MAIL_USERNAME'] = str(params[0])
#         app.config['MAIL_PASSWORD'] = str(params[1])
#         app.config['MAIL_SERVER']='smtp-mail.outlook.com'
#     else:
#         print("Error credenciales de correo")    
#     mail = Mail(app)

# def sendActivation(emailTo, cod):
#     host = "http://127.0.0.1:5000"
#     link = host + f"/activate?email={emailTo}&cod={cod}"
#     email = "aarnedoe@uninorte.edu.co"
#     try:
#         msg = Message('ACTIVA TU CUENTA!', sender=email, recipients=[emailTo])
#         msg.body = f"Activa tu cuenta mediante este enlace {link}"
#         mail.send(msg)
#         return True
#     except Exception as ex:
#         print(ex)
#         return False


# def sendReset(emailTo):
#     host = "http://127.0.0.1:5000"
#     link = host + f"/change?email={emailTo}"
#     email = "aarnedoe@uninorte.edu.co"
#     try:
#         msg = Message('CAMBIO DE CONTRASEÑA', sender=email, recipients=[emailTo])
#         msg.body = f"Cambia tu contraseña mediante este link {link}"
#         mail.send(msg)
#         return True
#     except Exception as ex:
#         print(ex)
#         return False
