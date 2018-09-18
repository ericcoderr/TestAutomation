#-*- encoding=utf-8 -*-  
# read yaml file
import unittest
# from src.helper import HTMLTestRunner
from src.helper.case_helper import Case

from src.common.constant import Field
# import codecs
from src.driver import MyDriver
import time
import os
import configparser
import sys
import shutil
from src.helper.file_names_helper import fileNames
import re


class BaseCase:
    def iterator_dynamic_testcase_new(self,file,test_case_list,driver,testunit,report_file):
        #Only generate one report
        dynamic_testcase = type(os.path.basename(file), (Case,), {})
        for test_case in test_case_list:
            if Field.SET_UP in test_case:
                setattr(dynamic_testcase, 'setUp',Case.exec_cmd(test_case[Field.SET_UP]))
            if Field.TEAR_DOWN in test_case:
                setattr(dynamic_testcase, 'tearDown',Case.exec_cmd(test_case[Field.TEAR_DOWN]))
            setattr(dynamic_testcase, 'test_'+test_case[Field.TESTCASE_NAME],Case.getTestFunc(driver, test_case,report_file))
        testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(dynamic_testcase))

    def iterator_dynamic_testcase(self,file,test_case_list,device):
        fr= None
        driver=None
        try:
            testunit = unittest.TestSuite()
            dynamic_testcase = type(os.path.basename(file), (Case,), {})
            driver = MyDriver.get_driver(device)
            report_file = self.get_report_filename(file,device)
            for test_case in test_case_list:
                #case = Case()

                # if Field.APP_PACKAGE in test_case:
                    # package= test_case[Field.APP_PACKAGE]
                    # activity= test_case[Field.APP_ACTIVITY]
                    # driver.start_activity(package, activity)
    #             case.param=test_case
    #             case.driver=driver
                #self.control = Control(self)
                #self.action = Actions(self)
                #self.expectation = Expectation(self)
                #setattr(dynamic_testcase, 'setUp',getattr(case,'setUp'))
                #setattr(dynamic_testcase, 'tearDown',getattr(case,'tearDown'))
                if Field.SET_UP in test_case:
                    setattr(dynamic_testcase, 'setUp',Case.exec_cmd(test_case[Field.SET_UP]))
                if Field.TEAR_DOWN in test_case:
                    setattr(dynamic_testcase, 'tearDown',Case.exec_cmd(test_case[Field.TEAR_DOWN]))

                setattr(dynamic_testcase, 'test_'+test_case[Field.TESTCASE_NAME],Case.getTestFunc(driver, test_case,report_file))
            testunit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(dynamic_testcase))
            fr = codecs.open(report_file,'wb','utf8')
            runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title='自动化测试报告', description='用例执行结果:',report_file_name=report_file)
            runner.run(testunit)
        finally:
            fr.close()
            driver.quit()


    '''
    Report path
    '''
    def get_report_filename(self,file,device):
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        workingPath =os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))
        s=re.findall(r'(.+?testcase)', str(file))
        s=os.path.join(s[0],os.pardir)
        reports_base_path = s + '/result/report/'
        report_path =  reports_base_path + date + '/'
        screenshot_path = reports_base_path + date + '/image/'
        case_name = os.path.basename(file)[:-5]

        if not os.path.exists(reports_base_path):      os.mkdir(reports_base_path)
        if not os.path.exists(report_path):            os.mkdir(report_path)
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)
            shutil.copy(workingPath + r'/pictures/Wal-mart.jpg',screenshot_path + r'logo.jpg')
        iniparser = configparser.ConfigParser()
        iniparser.read(s + '/config/apps_tag_info.ini')
        appsTagInfo = iniparser.get('test_app_version','tagNo')
        devices_info= device[Field.DEVICE_NAME]+'_'+str(device[Field.PLATFORM_VERSION])
        filename = fileNames()
        report_file_name = report_path + filename.generateReportName(deviceType=devices_info, svnVersion=appsTagInfo, caseName=case_name)
        return report_file_name
