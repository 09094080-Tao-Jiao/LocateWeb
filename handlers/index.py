import tornado.web
from models.entity import Entity

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        guid = self.get_argument('guid')
        self.render('index.html', guid =  guid)
