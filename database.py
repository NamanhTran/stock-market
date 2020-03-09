class Database:
    def __init__(self, app, mysql):
        self.app = app
        self.mysql = mysql
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'Namanhtran1!'
        app.config['MYSQL_DATABASE_DB'] = 'STOCK_TRADER'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)
        self.conn = mysql.connect()
    
    def execute(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        cursor.close()
        return data