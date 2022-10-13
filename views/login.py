from flask import Blueprint, request, render_template, session, redirect, flash, url_for
from controllers.pwdController import validatePwd

login = Blueprint('login',__name__, template_folder='templates')

@login.get('/login')
def loginForm():
    return render_template('index.html')

@login.post('/login')
def loginPost():
    email = request.form["email"]
    pwd = request.form["contrasenia"]
    if(validatePwd(email,pwd)):
        session["user"] = email
        return redirect(url_for("messages.inboxUser"))
    else:
        flash("Error de autenticación!",'error')
        return redirect(url_for("login.loginForm"))   


@login.get('/logout')
def logout_user():
    session.clear()
    flash('Sesión cerrada!','info')
    return redirect(url_for("login.loginForm"))             
