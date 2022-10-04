from flask import Blueprint, request
from app.controllers.dbController import changePassword

reset = Blueprint('reset', __name__, template_folder='templates')


@reset.post('/change')
def changePwd():
    data = {}
    data["email"] = request.form["email"]
    data["password"] = request.form["password"]
    if(changePassword(data)):
        return "Contraseña cambiada!"
    else:
        return "Error al cambiar contraseña!"


@reset.get('/reset')
def sendLink():
    return "Formulario de de email"


@reset.get('/change')
def getLink():
    data = {}
    data["email"] = request.args.get('email')
    return "Formulario de cambio de contraseña", data
