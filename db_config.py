import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='flaskdb1',
        # cursorclass=pymysql.cursors.DictCursor
    )
