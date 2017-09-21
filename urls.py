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
from handlers.manager import WhiteListIndexHandler
from handlers.manager import WhiteListHandler
from handlers.manager import WhiteListDetailsIndexHandler
from handlers.manager import WhiteListDetailsQueryHandler



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
    (r'/whitelist/index', WhiteListIndexHandler),
    (r'/whitelist/query', WhiteListHandler),
    (r'/whitelist/check', WhiteListHandler),
    (r'/whitelist/details/index', WhiteListDetailsIndexHandler),
    (r'/whitelist/details/query', WhiteListDetailsQueryHandler),
    (r'/', ReportHandler),
]
