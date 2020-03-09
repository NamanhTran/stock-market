from flask_mysqldb import MySQL

class Database:
    def __init__(self, app):
        self.app = app
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'Namanhtran1!'
        app.config['MYSQL_DB'] = 'STOCK_TRADER'
        self.mysql = MySQL(app)
        print(self.mysql)
    
    def execute(self, query, *args):
        cursor = self.mysql.connection.cursor()
        print(args)
        cursor.execute(query, *args)
        data = cursor.fetchall()
        cursor.close()
        return data