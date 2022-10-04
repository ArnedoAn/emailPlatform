from flask import Blueprint, request, session
from app.controllers.dbController import sendMail

send = Blueprint('send',__name__,template_folder='templates')

@send.post('/send')
def sendEmailUser():
    if "user" in session:
        data = {}
        data["to_user"] = request.form["to_user"]
        data["from_user"] = session['usuario']
        data["asunto"] = request.form["asunto"]
        data["cuerpo"] = request.form["cuerpo"]
        data["estado"] = request.form["estado"]
        data["fecha"] = request.form["fecha"]
        if(sendMail(data)):
            return "Enviado!"
        else:
            return "Error al enviar correo!"   
    else:
        return "Inicia sesión!"