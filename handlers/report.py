import tornado.web
from models.entity import Entity
import dba.mongodb
from bson.json_util import dumps

class ReportHandler(tornado.web.RequestHandler):
    def get(self):
        db = dba.mongodb.MongoDB().get_db()
        guid = self.get_argument('guid')
        records = dba.mongodb.MongoDB().get_many_docs(db,"tdiFiles",{"GUID":guid})
        #self.write(dumps(records))

        sqlCommand=("SELECT DATEDIFF(MINUTE,[StartOn],[EndOn]) AS ExecMinute,[Computer],[UserName],[Mac],"
                   "LogType,LogMessage,StartOn,EndOn,GUID,IsAuto "
                   "FROM [ITCommon].[dbo].[tdiLog] WITH(NOLOCK) "
                   "WHERE GUID='%s'") \
                   % (guid)
        mssql=dba.mssql.MSSQL()
        log = mssql.ExecQuery(sqlCommand)

        #self.render('report.html',records=dumps(records),execMinute=str(log[0][0]),StartOn=str(log[0][6]),EndOn=str(log[0][7]))
        self.render('report.html',records=records,count=records.count(),execMinute=str(log[0][0]),Computer=str(log[0][1]),UserName=str(log[0][2]),StartOn=str(log[0][6]),EndOn=str(log[0][7]))