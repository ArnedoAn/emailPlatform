from app import app
from controllers.dbController import select
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

def makePwd(pwd):
    return bcrypt.generate_password_hash(pwd)

def validatePwd(user,pwd):
    bdPwd = select(user)
    return bcrypt.check_password_hash(bdPwd,pwd)    