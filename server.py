#coding:utf-8

import tornado.ioloop
import tornado.options
from tornado.options import define, options
from application import application
import tornado.autoreload

define("port", default=8000, help="run on the given port", type=int)
if __name__ == "__main__":
    #tornado.options.parse_command_line()
    application.listen(options.port)
    print('Development server is running at http://127.0.0.1:%s/' % options.port)
    print('Quit the server with CONTROL-C')

    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()
