from flask import Blueprint, request, redirect, url_for, flash
from controllers.dbController import activation


activate = Blueprint('activate', __name__, template_folder='templates')

@activate.get("/activate")
def activateUser():
    data = {}
    data["email"] = request.args.get('email')
    data["cod"] = request.args.get('cod')
    if(activation(data)):
        flash("Activación exitosa!", 'message')
        return redirect(url_for("login.loginForm"))
    else:
        flash("Proceso de activación incorrecto!", 'error')
        return redirect(url_for("home"))    

    