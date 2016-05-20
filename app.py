import tornado.ioloop
import tornado.web
import pymysql
import os
import json

from collections import OrderedDict

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
        self.render(os.path.join(TEMPLATE_DIR, 'index.html'), fields=fields)

class SearchHandler(BaseHandler):
    def get(self):
        arguments = {item: self.get_argument(item) for item in self.request.arguments}
        settings = json.load(open(os.path.join(BASE_DIR, 'settings.json')))
        search_fields = settings['search_fields']

        sql = """
        select
            imonomy_data.id,
            networks.name as network,
            publishers.name as publisher,
            websites.name as website,
            domains,
            os_name,
            device_name
        from imonomy_data
        left join networks on imonomy_data.network_id = networks.id
        left join publishers on imonomy_data.publisher_id = publishers.id
        left join websites on imonomy_data.website_id = websites.id
        """
        sql_join = ""
        sql_filter = ""
        datas = []
        for argument in arguments:
            fieldName = argument
            data = arguments[argument]
            if not data:
                continue
            datas.append(data)
            sql_filter += """
            and imonomy_data.{fieldName} = %s
            """.format(fieldName=fieldName)

        sql += sql_join + "where true " + sql_filter
        result = None
        with db.cursor() as cursor:
            cursor.execute(sql, datas)
            result = cursor.fetchall()
        self.render(os.path.join(TEMPLATE_DIR, 'result.html'), result=result)

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
        (r"/search/", SearchHandler, dict(db=db, database_schema=get_databese_schema(db))),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
