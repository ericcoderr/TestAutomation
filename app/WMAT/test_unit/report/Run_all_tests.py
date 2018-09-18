#coding:utf-8
import unittest
import time
import sys
from src.helper import HTMLTestRunner 
import os
from src.helper.case_helper import Case
from src.helper import json_helper
casepath = "."
result = "d:/20161028"

def Createsuite():
    #定义单元测试容器
    testunit = unittest.TestSuite()
    #定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(casepath, pattern='test_*.py', top_level_dir=None)
    #将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        print(testunit)
    #test1 = '<unittest.suite.TestSuite tests=[<test_hello.Hello testMethod=testHello>]>'
   
    #testunit.addTest(test1)
    return testunit

#动态执行的函数，这里可以传入hash，实际在这里面解析和执行
def make_test_function(str, a, b):
    def test(self):
        json = '{"testcase_name":"wmat.testcases.RegsiterAndLogin","scenarios_suite":[{"scenarios_name":"wmat.scenarios.RegisterAndLogin.Register_MobileVerification_FirstDigit_Positive","page_steps":[{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]","action":"click","step_desc":"允许通知"},{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]","action":"click","step_desc":"允许位置"},{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]","action":"type","data":"东莞","step_desc":"输入深圳"},{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]","action":"click","step_desc":"选择深圳"},				{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]","action":"wait","step_desc":"等待"},{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]","action":"click","step_desc":"选择账号"},				{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]","action":"click","step_desc":"选择登陆"},				{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]","action":"type","data":"18026587555","step_desc":"输入手机"},				{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.EditText[1]","action":"type","data":"a123456","step_desc":"输入密码"},				{"page":"wmat.pages.tabbar.MyAccount","element":"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.Button[1]","action":"click",					"expectation":{"value":"18026587555","element":"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]"},"step_desc":"下一步"}]}]}'
        Case(json_helper.json2dict(json))()
    return test

def Createsuite_new():
    #创建两个动态的方法，可以传入参数，比如实际上我们可以传入hash字符串返回
    testHi1 = make_test_function('Hi1', 1, 1)
    # testHi2 = make_test_function('Hi2', 1, 2)
    
    #动态创建一个TestCase的子类，可以至指定类名
    dynamic_testcase = type('LoginTestCase', (unittest.TestCase,), {})
    #dynamic_testcase.testHi1 = testHi1
    #dynamic_testcase.testHi2 = testHi2
    
    #给动态的类添加testxxx方法
    setattr(dynamic_testcase, 'testHia', testHi1)
    # setattr(dynamic_testcase, 'testHib', testHi2)

    
    #最后用runner 调用这个suite执行，得到report
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(dynamic_testcase))
    print (testunit)
    return testunit

test_case = Createsuite_new()
#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#定义个报告存放路径，支持相对路径
tdresult = result + day
if os.path.exists(tdresult):
    filename = tdresult + "/" + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行结果：')
    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件
else:
    #os.mkdir(tdresult)
    filename = tdresult + "/" + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行结果：')
    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件