# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Login(unittest.TestCase):

    '''
    如果是selenium ide 录制的脚本，会包含以下代码，可以不管，当QA人员编写TestCase时不写这个方法
    '''
    # def setUp(self):
    #     self.driver = webdriver.Remote("http://192.168.21.51:4444/wd/hub", desired_capabilities=webdriver.DesiredCapabilities.PHANTOMJS)
    #     self.base_url = "http://192.168.19.123:8080/djoms"
    #     self.driver.implicitly_wait(30)
    #     self.verificationErrors = []
    #     self.accept_next_alert = True

    def test_login(self):
        print("test_login")
        print("----------------------------")
        driver = self.driver
        driver.get(self.base_url + "/djoms/login")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("oms1059")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("oms1059")
        driver.find_element_by_id("Submit").click()
        #self.assertEqual(u"指派 定案 打印发货单 过POS机 跟踪", driver.find_element_by_id("webctx_ordertab_head").text)
        self.assertEqual(u"指派", driver.find_element_by_id("tdTabAssign").text)

        #try: self.assertEqual("", driver.title)
        #except AssertionError as e: self.verificationErrors.append(str(e))

    def test_login1(self):
        print("test_login1")
        print("++++++++++++++++++++++")
        driver = self.driver
        driver.get(self.base_url + "/djoms/login")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("oms1059")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("oms1059")
        driver.find_element_by_id("Submit").click()
        #self.assertEqual(u"指派 定案 打印发货单 过POS机 跟踪", driver.find_element_by_id("webctx_ordertab_head").text)
        self.assertEqual(u"指派", driver.find_element_by_id("tdTabAssign").text)

        #try: self.assertEqual("", driver.title)
        #except AssertionError as e: self.verificationErrors.append(str(e))

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
