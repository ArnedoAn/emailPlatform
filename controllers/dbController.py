import sqlite3

def init_db():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


def insert(data):
    connection = init_db()
    cursor = connection.cursor()
    try:
        cursor.execute('SQL;')
        connection.commit()
        connection.close()
        return True
    except:
        connection.rollback()
        connection.close()
        return False
    


#SELECT
def select(data):
    connection = init_db()
    cursor = connection.cursor() 
    cursor.execute('SQL;')
    rows = cursor.fetchall()
    connection.close()
    return rows



