from flask import Blueprint, render_template, request, session
from app.controllers.dbController import sendMail

send = Blueprint('send',__name__,template_folder='templates')

@send.post('/send')
def sendEmailUser():
    if "user" in session:
        data = {}
        data["to_user"] = request.form["to_user"]
        data["from_user"] = session['user']
        data["asunto"] = request.form["asunto"]
        data["cuerpo"] = request.form["mensaje"]
        data["estado"] = request.form["estado"]
        data["fecha"] = request.form["fecha"]
        if(sendMail(data)):
            return "Enviado!"
        else:
            return "Error al enviar correo!"   
    else:
        return "Inicia sesión!"


@send.get('/send')
def sendEmailRender():
    return render_template('/inbox/enviar.html')

