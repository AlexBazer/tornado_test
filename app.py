import tornado.ioloop
import tornado.web
import pymysql
import os
import json

db = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='imonomy_db',
                             cursorclass=pymysql.cursors.DictCursor)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, db, database_schema):
        self.db = db
        self.database_schema = database_schema

class IndexHandler(BaseHandler):
    def get(self):
        fields = {}
        settings = json.load(open(os.path.join(BASE_DIR, 'settings.json')))
        for field in settings['search_fields']:
            fieldName, refTable = field.get('name'), field.get('reference_table')

            if not self.database_schema.get(fieldName):
                continue
            if 'int' in self.database_schema[fieldName]:
                fields[fieldName] = list(get_field_data(self.db, refTable))
            else:
                fields[fieldName] = fieldName
        print fields
        self.render(os.path.join(TEMPLATE_DIR, 'index.html'), fields=fields)


def get_field_data(db, refTable):
    with db.cursor() as cursor:
        query = "select * from {};".format(refTable)
        cursor.execute(query)
        return cursor.fetchall()


def get_databese_schema(db):
    database_schema = None
    with db.cursor() as cursor:
        query = 'describe imonomy_data;'
        cursor.execute(query)
        database_schema = cursor.fetchall()
    return {field['Field']:field['Type'] for field in database_schema}

def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler, dict(db=db, database_schema=get_databese_schema(db))),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
