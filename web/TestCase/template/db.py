import pymssql
import unittest
import base64

class Db(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        pwd = b'SGRwYXNzMTAxJA=='
        #self.base64_decode()
        conn = pymssql.connect(host='192.168.19.109',user='hddev',password= self.base64_decode(pwd),database='DJ_rfdb')
        self.conn = conn

    #加密，先执行这个方法把密码加密，然后在setUp里写死密文，传入数据库时解密
    def base64_encode(self,pwd):
        bytesString = pwd.encode(encoding="utf-8")
        b = base64.b64encode(bytesString)
        return b

    def base64_decode(self,pwd):
        decodestr = base64.b64decode(pwd)
        return decodestr.decode()

    def test_del_record(self):
        cur = self.conn.cursor()
        sql = "DELETE FROM ofs_lock WHERE store_nbr=1010"
        n = cur.execute(sql)
        print(n)
        print(cur.rowcount)
        cur.close()
        self.conn.commit()

    def test_qry(self):
        sql="SELECT * FROM ofs_lock"
        cur=self.conn.cursor()
        cur.execute(sql)
        print(cur.fetchall())
        cur.close()

    def test_insert(self):
        sql = "INSERT INTO ofs_lock(store_nbr,status,utime)VAlUES(%d,%d,getdate()) " %(3,13)
        cur=self.conn.cursor()
        cur.execute(sql)
        print(cur.rowcount)
        cur.close()
        self.conn.commit()


    def tearDown(self):
        self.conn.close()

if __name__ == "__main__":
    # db = Db()
    # pwd = db.base64_encode("Hdpass101$")
    # print(pwd)
    unittest.main()
