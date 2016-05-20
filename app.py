import tornado.ioloop
import tornado.web
import pymysql
import os

db = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='imonomy_db',
                             cursorclass=pymysql.cursors.DictCursor)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

class MainHandler(BaseHandler):
    def get(self):
        with self.db.cursor() as cursor:
            query = 'select count(*) from imonomy_data;'
            cursor.execute(query)
            print cursor.fetchall()
        self.render(os.path.join(TEMPLATE_DIR, 'index.html'))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler, dict(db=db)),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
