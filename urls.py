#coding:utf-8

from handlers.index import MainHandler
from handlers.find import FindHandler

urls = [
    (r'/', MainHandler),
    (r'/find', FindHandler),
]
