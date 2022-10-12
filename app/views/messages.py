from flask import Blueprint, session, render_template, flash, redirect, url_for
from app.controllers.dbController import inbox

messages = Blueprint('messages', __name__, template_folder='templates')

# @messages.get('/inbox')
# def leerinbox():
#     return render_template('/inbox/leer.html')

@messages.get('/inbox')
def inboxUser():
    if "user" in session:
        email = session["user"]
        data = inbox(email)
        if(data != None):
            return render_template('/inbox/leer.html', data=data) #Agregar [data]
        else:
            flash("No tienes mensajes pendientes", 'message')
            return render_template('/inbox/leer.html')
    else:
        flash("Inicia sesión antes de realizar esta operación!", 'warning')
        return redirect(url_for('login.loginForm'))

