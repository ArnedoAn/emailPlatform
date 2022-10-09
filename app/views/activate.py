from flask import Blueprint, request, render_template
from app.controllers.dbController import activation


activate = Blueprint('activate', __name__, template_folder='templates')

@activate.get("/activate")
def activateUser():
    data = {}
    data["email"] = request.args.get('email')
    data["cod"] = request.args.get('cod')
    if(activation(data)):
        return render_template('/inbox/leer.html')
    else:
        return "Proceso de activación incorrecto!"    

    