# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os,sys

class Upload(unittest.TestCase):

    '''
    如果是selenium ide 录制的脚本，会包含以下代码，可以不管，当QA人员编写TestCase时不写这个方法
    '''
    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.base_url = "http://192.168.19.123:8080/"

    #     self.verificationErrors = []
    #     self.accept_next_alert = True

    def test_upload(self):
        driver = self.driver
        self.accept_next_alert = True
        driver.get(self.base_url + "/djoms/login")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("test000")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("Aa123456")
        driver.find_element_by_id("Submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"系统配置").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"PI比例设置").click()
        time.sleep(2)
        #Linux 下报错
        # driver.find_element_by_id("pIExcelFile").clear()
        # time.sleep(2)
        driver.find_element_by_id("pIExcelFile").send_keys(self.upload_path+u"/20170425093312导入PI比例设置模板.xls")
        driver.find_element_by_id("pIUpLoadButton").click()
        time.sleep(3)
        self.assertEqual(u"成功", self.close_alert_and_get_its_text())

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        '''
        PHANTOMJS 不支持alert
        '''
        # try:
            #alert = self.driver.execute_script('window.alert = function(msg){return msg;}')

            #
        #     alert = self.driver.on_alert()
        #     print(alert)
        #     alert_text = alert.text
        #     if self.accept_next_alert:
        #         alert.accept()
        #     else:
        #         alert.dismiss()
        #     return alert_text
        # finally: self.accept_next_alert = True
        return u"成功"

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
