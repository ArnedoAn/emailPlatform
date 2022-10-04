from flask import Blueprint, request
from app.controllers.dbController import changePassword, login

reset = Blueprint('reset', __name__, template_folder='templates')


@reset.get('/reset')
def sendLink():
    return "Formulario de email"


@reset.get('/change')
def getLink():
    data = {}
    data["email"] = request.args.get('email')
    if(login(data) != False):
        return "Formulario cambio de contraseña", data
    else:
        return "Correo no registrado!"


@reset.post('/change')
def changePwd():
    data = {}
    data["email"] = request.form["email"]
    data["password"] = request.form["password"]
    if(changePassword(data)):
        return "Contraseña cambiada!"
    else:
        return "Error al cambiar contraseña!"
