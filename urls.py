#coding:utf-8

from handlers.index import MainHandler
from handlers.find import FindHandler
from handlers.log import LogHandler
from handlers.report import ReportHandler
from handlers.manager import ManagerHandler
from handlers.manager import ManagerIndexHandler
from handlers.manager import ManagerCSVHandler
from handlers.manager import EtprdpHandler
from handlers.manager import SoftwareHandler

urls = [
    (r'/index', MainHandler),
    (r'/find', FindHandler),
    (r'/log', LogHandler),
    (r'/manager/index', ManagerIndexHandler),
    (r'/manager', ManagerHandler),
    (r'/manager/check', ManagerHandler),
    (r'/manager/download', ManagerCSVHandler),
    (r'/manager/etprdp', EtprdpHandler),
    (r'/manager/software', SoftwareHandler),
    (r'/', ReportHandler),
]
