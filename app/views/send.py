from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from app.controllers.dbController import sendMail

send = Blueprint('send', __name__, template_folder='templates')


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
            flash("Error al enviar correo!", 'error')
            return redirect(url_for('send.sendEmailRender'))
    else:
        flash("Inicia sesión antes de realizar esta operación!",'warning')
        return redirect(url_for('home'))


@send.get('/send')
def sendEmailRender():
    return render_template('/inbox/enviar.html')
