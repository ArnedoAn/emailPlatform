from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from controllers.dbController import changePassword, login
from controllers.pwdController import makePwd
reset = Blueprint('reset', __name__, template_folder='templates')


@reset.get('/reset')
def sendLink():
    return render_template('auth/contraseña.html')


@reset.get('/change')
def getLink():
    data = None

    if "emailreset" in session:
        data = session["emailreset"]
    else:
        data = request.args.get('email')

    if(login(data) != False):
        session["emailreset"] = data
        return render_template('/auth/cambiocontraseña.html')
    else:
        flash("Correo no registrado!", 'error')
        return render_template('/auth/cambiocontraseña.html')


@reset.post('/change')
def changePwd():
    data = {}
    data["email"] = session["emailreset"]
    data["password"] = request.form["cambcontraseña"]
    data["pw1"] = request.form["confirmar"]
    if (data["password"] != data["pw1"]):
        flash("Las contraseñas no coinciden", 'message')
        return redirect(url_for('reset.getLink'))
    data["password"] = makePwd(data["password"])
    if(changePassword(data)):
        session.clear()
        flash("Constraseña cambiada!", 'message')
        return redirect(url_for('login.loginForm'))
    else:
        session.clear()
        flash("No se pudo cambiar la constraseña", 'error')
        return redirect(url_for('home'))
