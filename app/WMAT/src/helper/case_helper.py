#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time, _thread, os
import traceback
import unittest
from time import sleep
from src.common.constant import Field
from src.common.constant import CONFIG
from src.pages.actions import Actions
from src.pages.control import Control
from src.pages.expectation import Expectation
from src.helper.logging_helper import LoggingHelper
from asyncio.log import logger


class Case(unittest.TestCase):

    @staticmethod
    def exec_cmd(cmd):
        def run_cmd(self):
            print(cmd)
        return run_cmd

    @staticmethod
    def getTestFunc(driver,param,report_file_name):
        def func(self):
            self.driver=driver
            self.param = param
            self.report_file_name=report_file_name
            self.control = Control(self)
            self.action = Actions(self)
            self.expectation = Expectation(self)
            self._run_test_case()
        return func

    def setUp(self):
        LoggingHelper.get_logger().debug('setUp:'+self._testMethodName)
        print('setUp:'+self._testMethodName)
#         try:
# #             self.control = Control(self)
# #             self.action = Actions(self)
# #             self.expectation = Expectation(self)
#         except  BaseException:
#             exstr = traceback.format_exc()
#             print(exstr)
#             self.fail(exstr)


    def tearDown(self):
        LoggingHelper.get_logger().debug('tearDown:'+self._testMethodName)
        print('tearDown:'+self._testMethodName)
        self.driver.reset()
        #self.driver.quit()

    '''
    default runTest
    '''
    def _run_test_case(self):
        try:
            report_file_name=self.report_file_name
            testcase_hash=self.param
            scenarios_suite = testcase_hash[Field.SCENARIOS_SUITES]
            for scenarios in scenarios_suite:
                page_steps = scenarios[Field.PAGE_STEPS]
                for page_step in page_steps:
                    #find the element if exist
                    this_element=''
                    if Field.ELEMENT in page_step:
                        element = page_step[Field.ELEMENT]
                        this_element = self.control.find_element(element,Expectation.has_ios_name(page_step))
                    # find the data if exist
                    if Field.DATA in page_step:
                        data = page_step[Field.DATA]
                    else:
                        data = ''
                    # find the action if exist
                    if Field.ACTION in page_step:
                        action = page_step[Field.ACTION]
                        self.action.disptach_action(this_element, action, data)
                    #find the exceptation if exist
                    if Field.EXPECTATION in page_step:
                        expectations = page_step[Field.EXPECTATION]
                        for expectation in expectations:
                            flag = self.expectation.check(expectation,report_file_name)
                            self.assertTrue(flag)
                    #throw a exception when both exceptation or action is not exist
                    if not Field.ACTION in page_step and not Field.EXPECTATION in page_step:
                        self.fail("no EXPECTATION and ACTION")
                    if Field.STEP_DESC in page_step:
                        LoggingHelper.get_logger().debug('msg:%s | %s',time.strftime('%Y-%m-%d %H:%M:%S'),str(page_step[Field.STEP_DESC]))
                        print(time.strftime('%Y-%m-%d %H:%M:%S') + '|'+str(page_step[Field.STEP_DESC]))
                    else:
                        action=''
                        if Field.ACTION in page_step:
                            action=page_step[Field.ACTION]
                        LoggingHelper.get_logger().debug('msg:%s | %s | %s',time.strftime('%Y-%m-%d %H:%M:%S'),page_step[Field.PAGE],action)
                        print(time.strftime('%Y-%m-%d %H:%M:%S') + '|'+page_step[Field.PAGE]+'|'+action)
        except  BaseException:
            exstr = traceback.format_exc()
            LoggingHelper.get_logger().error('msg:%s',exstr)
            self.fail(exstr)

    def take_screenshots(self, counter, interval):
        i = 0
        try:
            while i < counter:
                filepath = os.path.abspath(CONFIG.TEMP_PIC_DIR + "screenshot%d.png"%i)
                print(time.strftime('%Y-%m-%d %H:%M:%S ') + filepath)
                self.driver.get_screenshot_as_file(filepath)
                sleep(interval)
                i += 1
        except BaseException as e:
            print(e)
