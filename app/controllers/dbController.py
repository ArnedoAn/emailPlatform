import sqlite3

def init_db():
    connection = sqlite3.connect('emaildb.db')
    #connection.row_factory = sqlite3.Row()
    return connection

def getSenderParams(token):
    connection = init_db()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "SELECT email,pwd FROM admin WHERE token = ?", [token])
        admin = cursor.fetchone()
        return admin
    except Exception as ex:
        print(ex)
        return False


def registerUser(data):
    connection = init_db()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO usuario(nombreUsuario,email,password,estado) VALUES (?, ?, ?, ?)",
            [data['username'], data['email'], data['password'], "no activado"])
        connection.commit()
        connection.close()
        return True
    except Exception as ex:
        connection.rollback()
        connection.close()
        print(ex)
        return False


def login(data):
    connection = init_db()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "SELECT password FROM usuario WHERE email = ?", [data['email']])
        pwd = cursor.fetchone
        return pwd
    except Exception as ex:
        print(ex)
        return False


def inbox(data):
    connection = init_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mensaje WHERE to_User = ?", [data])
    return cursor.fetchall


def sendMail(data):
    connection = init_db()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO mensaje(to_User,from_user,Asunto,cuerpo,estado,fecha)" +
                       " VALUES (?, ?, ?, ?, ?", [data["to_user"], data["from_user"],
                                                  data["asunto"], data["cuerpo"], data["estado"], data["fecha"]])
        connection.commit()
        connection.close()
        return True
    except Exception as ex:
        connection.rollback()
        connection.close()
        print(ex)
        return False


def changePassword(data):
    connection = init_db()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE usuario SET password = ? WHERE email = ?", 
            [data['password'], data['email']])
        connection.commit()
        connection.close()
        return True
    except Exception as ex:
        connection.rollback()
        connection.close()
        print(ex)
        return False


def activation(data):
    connection = init_db()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE usuario SET status = ? WHERE email = ? AND token = ?", 
            ['activado', data['email'], data['cod']])
        connection.commit()
        connection.close()
        return True
    except Exception as ex:
        connection.rollback()
        connection.close()
        print(ex)
        return False