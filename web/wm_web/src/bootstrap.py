#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import unittest
import time
import sys
import os
import types
from optparse import OptionParser

from unittest.suite import TestSuite

'''Only pthon 2.7.5 用到'''

if sys.version.startswith('2.7'):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    import ConfigParser
else:
    import configparser

work_path = os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))
sys.path.append(work_path)
bin_path = os.path.join(work_path,os.pardir,'bin')
sys.path.append(bin_path)
testcase_path = os.path.join(work_path,os.pardir,'TestCase')
sys.path.append(testcase_path)

from src.helper import HTMLTestRunner
from src.helper.logging_helper import LoggingHelper
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from src.constants.constants import Constants
import traceback
# import xmlrunner

global chromedriver
chromedriver = os.path.join(bin_path,'chromedriver.cmd')
class Bootstrap:

    if sys.version.startswith('2.7'):
        cfg = ConfigParser.ConfigParser()
    else:
        cfg = configparser.ConfigParser()
    args=sys.argv

    #方便在IDE里面调试，否则注释掉

    # args.append("--config")
    # args.append("template/config.ini")

    #如果命令行参数存在会覆盖这里

    '''此处如果先调用下面这句就会报导后面在调用添加的值无法赋值'''
    # (options, args) = parser.parse_args()
    parser = OptionParser()
    try:
        parser.add_option("--config", dest = "config", default = args[2])
        config = args[1]
        if config == "--config":
            config_path = args[2]
    except:
        print('必须指定config.ini')
        sys.exit(-1)
    os.chdir(testcase_path)
    cfg.read(config_path)

    #获取上传下载目录
    upload_path = "upload"
    download_path = "download"
    #upload_path = cfg.get('config',Constants.UPLOAD_PATH)
    #if len(upload_path) == 0:
    #     upload_path = "upload"
    # download_path = cfg.get('config',Constants.DOWNLOAD_PATH)
    # if len(download_path) == 0:
    #     download_path = "download"

    if config_path:
        parser.add_option("--server-env", dest = "server_env",default = cfg.get('config',Constants.WEB_TEST_ENV))
        #parser.add_option("--report", dest = "report",default =  cfg.get('config',Constants.REPORT_PATH))
        parser.add_option("--case-path", dest = "case_path",default = cfg.get('config',Constants.TEST_CASE_PATH))
        parser.add_option("--case-pattern", dest = "case_pattern",default = cfg.get('config',Constants.TEST_CASE_PATTERN))
        parser.add_option("--desc-sys", dest = "desc_sys",default = cfg.get('config',Constants.DESC_SYS))
        parser.add_option("--remote-host", dest = "selenium_server",default = cfg.get('config',Constants.SELENIUM_SERVER))
        parser.add_option("--desc-host", dest = "desc_host", default = cfg.get('config',Constants.DESC_HOST))
        #parser.add_option("--download", dest = "download_path",default = download_path)
        #parser.add_option("--upload", dest = "upload_path",default = upload_path)

        (options, args) = parser.parse_args()
    else:
        print('必须指定config.ini')
        sys.exit(-1)


    def boot_strap(self):
        ret_code = -1
        try:
            test_dir = Bootstrap.options.case_path
            sys.path.insert(0,test_dir)
            LoggingHelper.get_logger(Bootstrap.options.desc_sys).debug('Web test case bootstrap :%s %s','args:',Bootstrap.options)
            discover = unittest.defaultTestLoader.discover(test_dir, pattern = Bootstrap.options.case_pattern,top_level_dir = None)
            LoggingHelper.get_logger(Bootstrap.options.desc_sys).debug('Web test case bootstrap :%s %s','test_case:',discover)
            testunit = unittest.TestSuite()
            for test_suite in discover:
                if len(test_suite._tests) == 0:
                    continue
                for test_case in test_suite._tests:
                    #Must is TestSuite tests
                    #only one file all test_* method
                    if len(test_case._tests) == 0:
                        continue
                    dynamic_testcase = type(test_case._tests[0].__class__.__name__,(test_case._tests[0].__class__,),{})
                        #DB test_case ignore
                    if not 'Db' in test_case.__class__.__name__:
                        setattr(dynamic_testcase,'setUp',Bootstrap.setUp())
                after_set_up = unittest.defaultTestLoader.loadTestsFromTestCase(dynamic_testcase)
                testunit.addTest(after_set_up)

            fp = open(self.generate_report_file(), 'wb')

            #xml格式报告
            #xmlrunner.XMLTestRunner(output=fp).run(testunit)

            #html格式报告
            runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：')
            obj = runner.run(testunit)
            LoggingHelper.get_logger(Bootstrap.options.desc_sys).error('msg:%s',obj)
            if obj.failure_count > 0 or obj.error_count > 0:
                ret_code = obj.failure_count +obj.error_count
                return
            ret_code = 0
        except BaseException:
            exstr = traceback.format_exc()
            print(exstr)
            LoggingHelper.get_logger(Bootstrap.options.desc_sys).error('msg:%s',exstr)
            self.fail(exstr)
        finally:
            sys.exit(ret_code)


    @staticmethod
    def get_local_driver():
        options = webdriver.ChromeOptions()
        #options.add_argument(u'--user-data-dir=C:\\Users\\ehuan12\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
        options.add_argument('–first')
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

        #Download File
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.path.abspath(Bootstrap.get_download_path())}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(chromedriver,chrome_options=options)
        driver.implicitly_wait(30)
        return driver

    @staticmethod
    def get_remote_driver():
        desired_capabilities=webdriver.DesiredCapabilities.PHANTOMJS
        driver = webdriver.Remote(Bootstrap.options.selenium_server+"wd/hub", desired_capabilities=webdriver.DesiredCapabilities.PHANTOMJS)
        return driver

    @staticmethod
    def get_driver():
        if Bootstrap.options.server_env == 'server':
            return Bootstrap.get_remote_driver()
        else:
            return Bootstrap.get_local_driver()

    @staticmethod
    def get_base_url():
        return  Bootstrap.options.desc_host

    @staticmethod
    def setUp():
        def func(self):
            self.driver = Bootstrap.get_driver()
            self.base_url = Bootstrap.get_base_url()
            self.upload_path = Bootstrap.upload_path
            self.download_path = Bootstrap.get_download_path()
            self.verificationErrors = []
        return func

    @staticmethod
    def get_download_path():
        return os.path.join(os.pardir,Bootstrap.download_path,Bootstrap.options.desc_sys)

    #Generate report file name
    def generate_report_file(self):
        # test_report = Bootstrap.options.report
        # if len(test_report) == 0:
        #     test_report = os.path.join(os.pardir)
        #     test_report = os.path.join(test_report,os.pardir,"report")
        test_report = os.path.join(os.pardir,"report")
        report_sys = Bootstrap.options.desc_sys
        now_time = time.strftime('%H%M%S')#获取当前时间
        now_day = time.strftime('%Y%m%d')
        report_path = os.path.join(test_report,report_sys,now_day)
        if os.path.exists(report_path):
            pass
        else:
            os.makedirs(report_path)
        filename = os.path.join(report_path,now_time+'result.html')
        return filename


if __name__ == '__main__':
    bootstrap= Bootstrap()
    bootstrap.boot_strap()
