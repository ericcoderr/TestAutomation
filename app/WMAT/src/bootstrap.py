#-*- encoding=utf-8 -*-  
# read yaml file

import sys
import os
work_path=os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))
sys.path.append(work_path)
from src.helper.yaml_2json_helper import Yaml2JsonHelper
from src.base_case import BaseCase

from src.helper.logging_helper import LoggingHelper
from src.driver import MyDriver
from src.common.constant import GlobalVar
import unittest
from src.helper import HTMLTestRunner
import codecs
import time
import configparser
import re
from src.common.constant import Field
from src.helper.file_names_helper import fileNames
import shutil
from src.driver import MyDriver

'''
TestCase the entrance
'''

class Bootstrap:
    yaml2JsonHelper =  Yaml2JsonHelper()
    args=sys.argv
    if len(args) == 1:
        args.append('D:/TestAutomation/TestCase/GHS/Androidv1.8/testcase/')
        #args.append('register&login/Login.yaml')
        args.append('productdetails/P.yaml')
        args.append('huawei')

    def boot_strap(self):
        path=os.path.dirname(self.args[1])
        GlobalVar.YAML_PATH=path
        LoggingHelper.get_logger().debug('msg:%s%s','Start test case ...',self.args)
        sys.path.insert(0, os.path.join(path,os.path.pardir,'script'))
        #'account/*.yaml'
        Bootstrap.load_testcase_new(self,path,self.args[2])

    def load_testcase(self,path,file):
        result=[]
        files=Bootstrap.yaml2JsonHelper.find_files(path,result,file)
        for file in files:
            test_case_list=Bootstrap.yaml2JsonHelper.yaml_2json_test_case(file)
            LoggingHelper.get_logger().debug('msg:%s %s','test_case_list:',test_case_list)
            devices = Bootstrap.load_device(self,os.path.abspath(os.path.join(path,os.pardir,'config','devices.yaml')))
            LoggingHelper.get_logger().debug('msg:%s %s','devices info:',devices)
            for device in devices:
                BaseCase().iterator_dynamic_testcase(file,test_case_list,device)

    def load_testcase_new(self,path,file):
        devices = Bootstrap.load_device(self,os.path.abspath(os.path.join(path,os.pardir,'config','devices.yaml')))
        LoggingHelper.get_logger().debug('msg:%s %s','devices info:',devices)
        for device in devices:
            result=[]
            files=Bootstrap.yaml2JsonHelper.find_files(path,result,file)
            if len(files) == 0:
                return
            testunit = unittest.TestSuite()
            report_file = self.get_report_filename_new(files[0],device)
            fr=None
            driver=None
            try:
                test_case_file_list=[]
                for file in files:
                    print(file)
                    LoggingHelper.get_logger().debug('msg:%s %s','fie_name:',file)
                    test_case_file_list.append(Bootstrap.yaml2JsonHelper.yaml_2json_test_case(file))
                driver = MyDriver.get_driver(device)
                for test_case_list in test_case_file_list:
                    #test_case_list=Bootstrap.yaml2JsonHelper.yaml_2json_test_case(file)
                    #LoggingHelper.get_logger().debug('msg:%s %s','test_case_list:',test_case_list)
                    BaseCase().iterator_dynamic_testcase_new(file,test_case_list,driver,testunit,report_file)
                fr = codecs.open(report_file,'wb','utf8')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fr,title='自动化测试报告', description='用例执行结果:',report_file_name=report_file)
                runner.run(testunit)
            finally:
                if driver is not None:
                    driver.quit()
                if fr is not None:
                    fr.close()


        '''
    Report path
    '''
    def get_report_filename_new(self,file,device):
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
        report_file_name = report_path + filename.generate_report_name_without_case(deviceType=devices_info, svnVersion=appsTagInfo)
        return report_file_name

    def load_device(self,path):
        '''
        load device
        '''
        devices = MyDriver.get_devices(path,self.args[3])
        return devices

if __name__ == '__main__':
    bootstrap= Bootstrap()
    bootstrap.boot_strap()

