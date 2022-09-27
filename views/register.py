from flask import Blueprint, request
from controllers.dbController import insert
from controllers.pwdController import makePwd

register = Blueprint('register', __name__, template_folder='templates')

@register.get('/register')
def registerForm():
    return 'Form'

@register.post('/register')
def registerUser():
    email = request.form['email']
    name = request.form['name']
    pwd = request.form['pwd']
    pwd = makePwd(pwd)
    if(insert([email,name,pwd])):
        return 'Registrado!'
    else:
        return 'Error al registrar!'


############### COMPLETAR ##############        


