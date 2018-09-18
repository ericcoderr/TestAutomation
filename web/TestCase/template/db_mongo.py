
#coding=utf-8
from pymongo import MongoClient

class DbMongo(unittest.TestCase):
     def setUp(self):
        #建立MongoDB数据库连接
        client = MongoClient('localhost',27017)
        self.client = client

    def tearDwon(self):
        print('tearDown')

    def get_collection(self):
        #连接所需数据库,test为数据库名
        db=self.client.test
        #连接所用集合，也就是我们通常所说的表，test为表名
        collection=db.test
        return collection

#接下里就可以用collection来完成对数据库表的一些操作


    def test_insert(self):
        collection = self.get_collection
        #向集合中插入数据
        collection.insert({name:'Tom',age:25,addr:'Cleveland'})


if __name__ == "__main__":
    unittest.main()




