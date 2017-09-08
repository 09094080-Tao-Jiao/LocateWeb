from pymongo import MongoClient
from bson import BSON
from bson import json_util as jsonb

import sys
sys.path.append("..")
import config

class MongoDB:
    def __init__(self):
        self.host = config.mg_host
        self.port = config.mg_port
        self.user = config.mg_userid
        self.pwd = config.mg_password
        self.db = config.mg_name

    def get_db(self):
        #建立连接
        client = MongoClient(self.host, self.port)
        #client = MongoClient('mongodb://accountUser:password@localhost:8081/test?authMechanism=SCRAM-SHA-1')
        #test,还有其他写法
        db = client[self.db]
        return db

    def get_collection(self,db,col):
        #选择集合(mongo中collection和database都是lazy创建的，具体可以google下)
        collection = db[col]
        print(collection)

    def insert_one_doc(self,db,col,doc):
        #插入一个document
        posts = db[col]
        post_id = posts.insert(doc)
        print(post_id)
        return post_id

    def insert_mulit_docs(self,db,col,docs):
        #批量插入documents,插入一个数组
        posts = db[col]
        obj_ids = posts.insert(docs)
        print(obj_ids)

    ##查询，可以对整个集合查询，可以根ObjectId查询，可以根据某个字段查询等
    def get_all_colls(self,db):
        #获得一个数据库中的所有集合名称
        print(db.collection_names())

    def get_one_doc(self,db,col):
        #有就返回一个，没有就返回None
        posts = db[col]
        return posts.find_one()

    def get_one_by_id(self,db):
        #通过objectid来查找一个doc
        posts = db.posts
        obj = posts.find_one()
        obj_id = obj["_id"]
        print("_id 为ObjectId类型 :")
        print(posts.find_one({"_id":obj_id}))
        #需要注意这里的obj_id是一个对象，不是一个str，使用str类型作为_id的值无法找到记录
        print("_id 为str类型 ")
        print(posts.find_one({"_id":str(obj_id)}))

        #可以通过ObjectId方法把str转成ObjectId类型
        from bson.objectid import ObjectId
        print("_id 转换成ObjectId类型")
        print(posts.find_one({"_id":ObjectId(str(obj_id))}))

    def get_many_docs(self,db,col,docs):
        #mongo中提供了过滤查找的方法，可以通过各
        #种条件筛选来获取数据集，还可以对数据进行计数，排序等处理
        posts = db[col]
        #所有数据,按年龄排序, -1是倒序

        if len(docs)>0:
            all =  posts.find(docs)
        else:
            all =  posts.find()
        return all

        #条件查询
        #count = posts.find({"name":"lzz"}).count()
        #print("lzz: %s"%count)
        #for i in  posts.find({"name":"lzz", "age":{"$lt":20}}):
        #    print(i)

    def clear_coll_datas(self,db,col):
        #清空一个集合中的所有数据
        db[col].remove({})

if __name__ == "__main__":
    db = MongoDB().get_db()
    print(db)
    col = {"Computer":"C09094080","Mac":"SSSS","FileName":"A.TXT","FilePath":"C:\A.TXT"}
    MongoDB().insert_one_doc(db,"test",col)
    all = MongoDB().get_many_docs(db,"test","")
    print(jsonb.dumps(list(all)))
    #MongoDB().clear_coll_datas(db,"test")
