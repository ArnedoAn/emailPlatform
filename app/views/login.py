from flask import Blueprint, request, render_template, session
from app.controllers.pwdController import validatePwd

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
        return render_template('/inbox/leer.html')
    else:
        return "Error de autenticación!"    


@login.post('/logout')
def logout_user():
    session.clear()
    return "Sesión cerrada!"             
