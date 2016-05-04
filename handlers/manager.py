import tornado.web
from models.entity import Entity
import dba.mongodb
import dba.mssql
from bson.json_util import dumps
import random
import common.character

class ManagerIndexHandler(tornado.web.RequestHandler):
    def get(self):

        self.render('manager.html')

class ManagerHandler(tornado.web.RequestHandler):
    def get(self):

        emplid = self.get_argument('emplid')

        date_from = self.get_argument('date_from')
        date_to = self.get_argument('date_to')
        IsWF = self.get_argument('IsWF')
        company = self.get_argument('company')
        etprdp = self.get_argument('etprdp')
        IsCheck = self.get_argument('IsCheck')
        software = self.get_argument('software')


        where =" 1=1 "
        wherecount = " 1=1 "

        if len(IsCheck)!=0 :
            if IsCheck=='NNULL':
                where = where +(" AND IsCheck<>''Y'' ")
                wherecount = wherecount +(" AND IsCheck<>'Y' ")
            else:
                where = where +(" AND IsCheck=''%s'' ") % (IsCheck)
                wherecount = wherecount +(" AND IsCheck='%s' ") % (IsCheck)

        if len(software)!=0 :
            where = where + (" AND software=''%s'' ") % (software)
            wherecount = wherecount +(" AND software='%s' ") % (software)

        if len(IsWF)!=0 :
            where = where + (" AND IsWF=''%s'' ") % (IsWF)
            wherecount = wherecount +(" AND IsWF='%s' ") % (IsWF)

        if len(company)!=0 :
            where = where + (" AND company=''%s'' ") % (company)
            wherecount = wherecount +(" AND company='%s' ") % (company)

        if len(etprdp)!=0 :
            where = where + (" AND etprdp=''%s'' ") % (etprdp)
            wherecount = wherecount +(" AND etprdp='%s' ") % (etprdp)

        if len(emplid)!=0 :
            where = where + (" AND UserName=''%s'' ") % (emplid)
            wherecount = wherecount +(" AND UserName='%s' ") % (emplid)

        if len(date_from)!=0 and len(date_to)==0:
            where = where + (" AND CreateDay=''%s''") % (date_from)
            wherecount = wherecount+ (" AND CreateDay='%s'") % (date_from)

        if len(date_from)!=0 and len(date_to)!=0:
            where = where + (" AND CreateDay BETWEEN ''%s'' AND ''%s''") % (date_from,date_to)
            wherecount = wherecount + (" AND CreateDay BETWEEN '%s' AND '%s'") % (date_from,date_to)


        page = self.get_argument('page')
        rows = self.get_argument('rows')

        if len(where)!=0 :
            sqlCommand=("SELECT COUNT(*),COUNT(*)/%s FROM [ITCommon].[dbo].[View_tdiSoftwareScan_Python_Last]"
              "WHERE %s") \
            % (rows,wherecount)
        else:
            sqlCommand=("SELECT COUNT(*),COUNT(*)/%s FROM [ITCommon].[dbo].[View_tdiSoftwareScan_Python_Last]") \
            % (rows)


        mssql=dba.mssql.MSSQL()
        count = mssql.ExecQuery(sqlCommand)

        sqlCommand=("[dbo].[sys_Page_v2]  @PCount='%s',@RCount='%s'"
            ",@sys_Table='[ITCommon].[dbo].[View_tdiSoftwareScan_Python_Last]',@sys_Key='UID'"
            ",@sys_Fields='*',@sys_Where='%s'"
            ",@sys_Order='UID DESC',@sys_Begin='1'"
            ",@sys_PageIndex='%s',@sys_PageSize='%s'") \
            % (count[0][1],count[0][0],where,page,rows)

        files = mssql.ExecQueryDic(sqlCommand)

        results = {'total': count[0][0], 'rows': files};

        self.write(dumps(results))

    def post(self):

        uids = self.get_argument('uids')

        typeOP = self.get_argument('typeOP')

        if typeOP =="1":
            sqlCommand=("UPDATE  [dbo].[tdiFilesLast] SET IsCheck='Y' WHERE UID IN ('%s')")  % (uids.replace(",", "','"))
        elif typeOP =="2":
            sqlCommand=("UPDATE  [dbo].[tdiFilesLast] SET IsCheck='N' WHERE UID IN ('%s')")  % (uids.replace(",", "','"))
        else :
            sqlCommand=("UPDATE  [dbo].[tdiFilesLast] SET IsCheck='' WHERE UID IN ('%s')")  % (uids.replace(",", "','"))
        mssql=dba.mssql.MSSQL()
        mssql.ExecNonQuery(sqlCommand)
        self.write("true")

class ManagerCSVHandler(tornado.web.RequestHandler):
    '''
    @tornado.gen.coroutine
    def get(self):
        self.set_header('Content-Type','text/csv')
        self.set_header('content-Disposition','attachment; filename=dump.csv')
        self.write('lineNumber,measure\r\n') # File header
        for line in range(0,1000000):
            self.write(','.join([str(line), str(random.random())])+'\r\n') # mock data
            yield self.flush()
    '''

    @tornado.gen.coroutine
    def get(self):

        emplid = self.get_argument('emplid')
        date_from = self.get_argument('date_from')
        date_to = self.get_argument('date_to')
        IsWF = self.get_argument('IsWF')
        company = self.get_argument('company')
        etprdp = self.get_argument('etprdp')
        IsCheck = self.get_argument('IsCheck')
        software = self.get_argument('software')

        where =" 1=1 "

        if len(IsCheck)!=0 :
            if IsCheck=='NNULL':
                where = where +(" AND IsCheck<>'Y' ")
            else:
                where = where +(" AND IsCheck='%s' ") % (IsCheck)

        if len(software)!=0 :
            where = where +(" AND software=N'%s' ") % (software)

        if len(IsWF)!=0 :
            where = where +(" AND IsWF='%s' ") % (IsWF)

        if len(company)!=0 :
            where = where +(" AND company='%s' ") % (company)

        if len(etprdp)!=0 :
            where = where +(" AND etprdp='%s' ") % (etprdp)

        if len(emplid)!=0 :
            where = where +(" AND UserName='%s' ") % (emplid)

        if len(date_from)!=0 and len(date_to)==0:
            where = where+ (" AND CreateDay='%s'") % (date_from)

        if len(date_from)!=0 and len(date_to)!=0:
            where = where + (" AND CreateDay BETWEEN '%s' AND '%s'") % (date_from,date_to)


        if len(where)!=0 :
            sqlCommand=("SELECT * FROM [ITCommon].[dbo].[View_tdiSoftwareScan_Python_Last]"
              "WHERE %s") \
            % (where)
        else:
            sqlCommand=("SELECT * FROM [ITCommon].[dbo].[View_tdiSoftwareScan_Python_Last]")


        mssql=dba.mssql.MSSQL()
        files = mssql.ExecQueryDic(sqlCommand)

        self.set_header("Content-Type", 'text/csv; charset="utf8"')
        self.set_header('content-Disposition','attachment; filename=dump.csv')
        self.write(('是否合法,是否iWorkflow,Company,厂区,计算机名,登陆账号,Mac地址,创建日期,姓名,部门,软件,文件名,文件路径\r\n').encode('gb2312')) # File header
        for file in files:
            self.write((','.join([str(file['IsCheck']),
                                 str(file['IsWF']),
                                 str(file['company']),
                                 str(file['etprdp']),
                                 str(file['Computer']),
                                 "'"+str(file['UserName']),
                                 str(file['Mac']),
                                 str(file['CreateOn']),
                                 str(file['chinam']),
                                 str(file['shonam']),
                                 str(file['software']),
                                 str(file['FileName']),
                                 str(file['FilePath'])])+'\r\n').encode('gb2312'))
            yield self.flush()

class EtprdpHandler(tornado.web.RequestHandler):
    def get(self):

        sqlCommand=("SELECT 'ALL' as text,'' AS value  UNION SELECT DISTINCT etprdp AS text,etprdp AS value FROM  dbo.Emph WHERE company='QSMC' AND ISNULL(etprdp,'')<>'' ")
        mssql=dba.mssql.MSSQL()
        etprd = mssql.ExecQueryDic(sqlCommand)

        self.write(dumps(etprd))

class SoftwareHandler(tornado.web.RequestHandler):
    def get(self):

        sqlCommand=("SELECT '' as text,'' AS value  UNION SELECT DISTINCT Software AS text,Software AS value FROM  dbo.tdiFilesToSearch  WITH(NOLOCK)")
        mssql=dba.mssql.MSSQL()
        software = mssql.ExecQueryDic(sqlCommand)

        self.write(dumps(software))

