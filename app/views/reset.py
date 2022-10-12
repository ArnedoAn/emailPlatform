from flask import Blueprint, Flask, render_template, request, flash, redirect, url_for, session
from app.controllers.dbController import changePassword, login

reset = Blueprint('reset', __name__, template_folder='templates')


@reset.get('/reset')
def sendLink():
    return render_template('auth/contraseña.html')


@reset.get('/change')
def getLink():
    
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
    data["password"] = request.form["cambcontraseña"]
    data["pw1"] = request.form["confirmar"]
    if (data["password"] != data["pw1"]):
        flash("Las contraseñas no coinciden",'message')
        return render_template('/auth/cambiocontraseña.html')        
    if(changePassword(data)):
        flash("Constraseña cambiada!",'message')
        return redirect(url_for('login.loginform'))
    else:
        flash("No se pudo cambiar la constraseña", 'error')
        return redirect(url_for('home'))
