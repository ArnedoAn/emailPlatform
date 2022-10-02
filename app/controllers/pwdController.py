from flask import Flask
from controllers.dbController import login
from flask_bcrypt import Bcrypt

app = Flask(__name__)

bcrypt = Bcrypt(app)

def makePwd(pwd):
    return bcrypt.generate_password_hash(pwd)

def validatePwd(user,pwd):
    bdPwd = login(user)
    return bcrypt.check_password_hash(bdPwd,pwd)    