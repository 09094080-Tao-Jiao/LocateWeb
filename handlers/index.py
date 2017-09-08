import tornado.web
from models.entity import Entity
import dba.mongodb
import dba.mssql

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        guid = self.get_argument('guid')

        sqlCommand=("SELECT DATEDIFF(MINUTE,[StartOn],[EndOn]) AS ExecMinute,[Computer],[UserName],[Mac],"
                   "LogType,LogMessage,StartOn,EndOn,GUID,IsAuto "
                   "FROM [ITCommon].[dbo].[tdiLog] WITH(NOLOCK) "
                   "WHERE GUID='%s'") \
                   % (guid)
        mssql=dba.mssql.MSSQL()
        log = mssql.ExecQuery(sqlCommand)

        self.render('index.html', guid =  guid,execMinute=str(log[0][0]),StartOn=str(log[0][6]),EndOn=str(log[0][7]))