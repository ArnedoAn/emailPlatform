from controllers.dbController import login
from werkzeug.security import generate_password_hash, check_password_hash

def makePwd(pwd):
    return generate_password_hash(pwd)

def validatePwd(user,pwd):
    bdPwd = login(user)
    print(bdPwd)
    if bdPwd != None:
        return check_password_hash(bdPwd[0],pwd)
    else:
        print("Error en validar contraseña")
        return False        