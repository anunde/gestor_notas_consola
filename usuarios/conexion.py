import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="consolaapp",
        port="3306"
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]