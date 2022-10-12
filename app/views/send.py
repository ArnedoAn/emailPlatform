from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from app.controllers.dbController import sendMail
import time

send = Blueprint('send', __name__, template_folder='templates')



@send.post('/send')
def sendEmailUser():
    if "user" in session:
        data = {}
        data["to_user"] = request.form["to_user"]
        data["from_user"] = session['user']
        data["asunto"] = request.form["asunto"]
        data["cuerpo"] = request.form["mensaje"]
        data["estado"] = "no leido"
        data["fecha"] = time.strftime("%c")
        if(sendMail(data)):
            return redirect(url_for("messages.inboxUser"))
        else:
            flash("Error al enviar correo!", 'error')
            return redirect(url_for('send.sendEmailRender'))
    else:
        flash("Inicia sesión antes de realizar esta operación!",'warning')
        return redirect(url_for('home'))


@send.get('/send')
def sendEmailRender():
    return render_template('/inbox/enviar.html')
