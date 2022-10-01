import sqlite3


def init_db():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


def register(data):
    connection = init_db()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO usuario(nombreUsuario,email,password,estado) VALUES (?, ?, ?, ?)",
                       [data.username, data.email, data.password, "no activado"])
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
            "SELECT password FROM usuario WHERE email = ?", [data.email])
        pwd = cursor.fetchone
        return pwd
    except Exception as ex:
        print(ex)
        return False


def inbox(data):
    connection = init_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mensaje WHERE to_User = ?", [data.email])
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
            [data.password, data.email])
        connection.commit()
        connection.close()
        return True
    except Exception as ex:
        connection.rollback()
        connection.close()
        print(ex)
        return False


# def insert(data):
#     connection = init_db()
#     cursor = connection.cursor()
#     try:
#         cursor.execute('SQL;')
#         connection.commit()
#         connection.close()
#         return True
#     except:
#         connection.rollback()
#         connection.close()
#         return False


# SELECT
# def select(data):
#     connection = init_db()
#     cursor = connection.cursor()
#     cursor.execute('SQL;')
#     rows = cursor.fetchall()
#     connection.close()
#     return rows
