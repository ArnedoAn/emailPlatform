from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.controllers.dbController import changePassword, login

reset = Blueprint('reset', __name__, template_folder='templates')


@reset.get('/reset')
def sendLink():
    return render_template('auth/contraseña.html')


@reset.get('/change')
def getLink():
    data = {}
    data["email"] = request.args.get('email')
    if(login(data) != False):
        return render_template('/auth/cambiocontraseña.html')
    else:
        flash("Correo no registrado!", 'error')
        return redirect(url_for("reset.sendLink"))


@reset.post('/change')
def changePwd():
    data = {}
    data["email"] = request.form["email"]
    data["password"] = request.form["password"]
    if(changePassword(data)):
        flash("Constraseña cambiada!",'message')
        return redirect(url_for('home'))
    else:
        flash("No se pudo cambiar la constraseña", 'error')
        return redirect(url_for('home'))
