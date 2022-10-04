from flask import Blueprint, request, redirect
from app.controllers.dbController import registerUser
from app.controllers.pwdController import makePwd
from app.controllers.emailController import sendActivation
import secrets

register = Blueprint('register', __name__, template_folder='templates')

@register.get('/register')
def registerForm():
    return 'Form'

@register.post('/register')
def register_User():
    data = {}
    jsond = request.get_json()
    data['email'] = str(jsond["email"])
    data['username'] = str(jsond["username"])
    pwd = str(jsond['password'])
    # data.email = request.form['email']
    # data.username = request.form['name']
    data['token'] = secrets.token_urlsafe()
    # pwd = request.form['pwd']
    data['password'] = makePwd(pwd)
    if(registerUser(data)):
        if(sendActivation(data['email'],data['token'])):
            return 'Link de activación enviado!'
        else:
            return "Error al enviar link de activación"    
    else:
        return 'Template de mal registro'

    


