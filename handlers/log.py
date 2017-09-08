import tornado.web
from models.entity import Entity
import dba.mongodb
import dba.mssql
from bson.json_util import dumps

class LogHandler(tornado.web.RequestHandler):
    def get(self):
        guid = self.get_argument('guid')
        sqlCommand=("SELECT DATEDIFF(MINUTE,[StartOn],[EndOn]) AS ExecMinute,[Computer],[UserName],[Mac],"
                   "LogType,LogMessage,StartOn,EndOn,GUID,IsAuto "
                   "FROM [ITCommon].[dbo].[tdiLog] WITH(NOLOCK) "
                   "WHERE GUID='%s'") \
                   % (guid)
        mssql=dba.mssql.MSSQL()
        log = mssql.ExecQuery(sqlCommand)
        self.write(str(log[0][0]))


