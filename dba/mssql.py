#coding=utf-8
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name: pymssqlTest.py
# Purpose: 测试 pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
#
# Author: scott
#
# Created: 04/02/2012
#-------------------------------------------------------------------------------
#import sys   #引用sys模块进来，并不是进行sys的第一次加载
#reload(sys)  #重新加载sys
#sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数
import pymssql
import config

import _mssql
import uuid
import decimal

_mssql.__version__

class MSSQL:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：

    """

##    def __init__(self,host,user,pwd,db):
##        self.host = host
##        self.user = user
##        self.pwd = pwd
##        self.db = db

    def __init__(self,link="DB"):

        if link == "DB":
            self.host = config.db_host
            self.user = config.db_userid
            self.pwd = config.db_password
            self.db = config.db_name
        elif link == "HR":
            self.host = config.db_hr_host
            self.user = config.db_hr_userid
            self.pwd = config.db_hr_password
            self.db = config.db_hr_name
        else :
            self.host = config.db_host
            self.user = config.db_userid
            self.pwd = config.db_password
            self.db = config.db_name

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,timeout=50,login_timeout=2,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def __GetConnectDoc(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,timeout=50,login_timeout=2,charset="utf8")
        cur = self.conn.cursor(as_dict=True)
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur



    ##验证数据库连接
    def VerifyConnection(self):
        try:
            if self.host=='':
                return False
            conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,timeout=1,login_timeout=1,charset="utf8")
            return True
        except:
            return False

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecQueryDic(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnectDoc()

        cur.execute(sql)
        resList = cur.fetchall()
        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句
        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

    def ExecStoreProduce(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.commit()
        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

