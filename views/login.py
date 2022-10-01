from flask import Blueprint, request, render_template, session
from controllers.pwdController import validatePwd

login = Blueprint('login',__name__, template_folder='templates')

@login.get('/login')
def loginForm():
    return 'Form'

@login.post('/login')
def loginPost():
    email = request.form["email"]
    pwd = request.form["pwd"]
    if(validatePwd(email,pwd)):
        session["user"] = email
        session["logged"] = True
        return "Inicio de sesión exitoso!"
    else:
        return "Error de autenticación!"         
