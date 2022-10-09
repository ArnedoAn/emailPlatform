from flask import Blueprint, session, render_template
from app.controllers.dbController import inbox

messages = Blueprint('messages', __name__, template_folder='templates')

@messages.get('/inbox')
def inboxUser():
    if "user" in session:
        email = session["user"]
        data = inbox(email)
        if(data != None):
            return render_template('/inbox/leer.html', data)
        else:
            return "Usuario invalido"
    else:
        return "Inicia sesión!"        