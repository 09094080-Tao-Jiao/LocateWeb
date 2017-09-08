import tornado.web
from models.entity import Entity
import dba.mongodb
from bson.json_util import dumps

class FindHandler(tornado.web.RequestHandler):
    def get(self):
        db = dba.mongodb.MongoDB().get_db()
        #entity = dba.mongodb.MongoDB().get_many_docs(db,"tdiFiles",{"GUID":"c3a0f082-f32a-11e5-9ebc-b60c45fbeb0c"})
        guid = self.get_argument('guid')
        entity = dba.mongodb.MongoDB().get_many_docs(db,"tdiFiles",{"GUID":guid})
        #self.write(guid)
        self.write(dumps(entity))
        #self.write("test")