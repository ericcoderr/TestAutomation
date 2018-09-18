#coding:utf-8

import unittest

class Print(unittest.TestCase):


    #def setUp(self):
    #    print("1")
        
    #def tearDown(self):
    #    print("2")

    def testPrint(self):
        
        print("Hello World!")
        
    #def check_print_result(self, result, message):
    #   print("3")
    
    def test_str_empty(self):
        s=None
        ss=''
        sss='sasd'
        if None and len(s)==0:
            print('s is empty')
        if len(ss)==0:
            print('ss is empty')
        if len(sss)>0:
            print('sss not empty')

if __name__ == '__main__':
    unittest.main()
