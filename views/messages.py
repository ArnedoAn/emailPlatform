from flask import Blueprint, session
from controllers.dbController import inbox

messages = Blueprint('messages', __name__, template_folder='templates')

@messages.get('/inbox')
def inboxUser():
    email = session["user"]
    data = inbox(email)
    if(data != None):
        return "Plantilla", data
    else:
        return "Usuario invalido"