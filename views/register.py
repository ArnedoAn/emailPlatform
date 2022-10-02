from flask import Blueprint, request, redirect
from controllers.dbController import registerUser
from controllers.pwdController import makePwd
from controllers.emailController import sendActivation
import secrets

register = Blueprint('register', __name__, template_folder='templates')

@register.get('/register')
def registerForm():
    return 'Form'

@register.post('/register')
def register_User():
    data= {}
    data.email = request.form['email']
    data.username = request.form['name']
    data.token = secrets.token_urlsafe()
    pwd = request.form['pwd']
    data.password = makePwd(pwd)
    if(registerUser(data)):
        if(sendActivation(data.email,data.token)):
            return 'Link de activación enviado!'
        else:
            return "Error al enviar link de activación"    
    else:
        return 'Template de mal registro'

    


