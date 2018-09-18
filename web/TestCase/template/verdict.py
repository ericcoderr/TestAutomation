# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Verdict(unittest.TestCase):
    '''
    如果是selenium ide 录制的脚本，会包含以下代码，可以不管，当QA人员编写TestCase时不写这个方法
    '''
    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.implicitly_wait(30)
    #     self.base_url = "http://192.168.19.123:8080"
    #     self.verificationErrors = []
    #     self.accept_next_alert = True

    def test_verdict(self):
        driver = self.driver

        #login
        driver.get(self.base_url + "/djoms/")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("oms1059")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("oms1059")
        driver.find_element_by_id("Submit").click()
        driver.find_element_by_id("webctx_ordertab_body").click()

        # driver.find_element_by_link_text(u'定案').click()
        driver.find_element_by_xpath(".//*[@id='tdTabFinalize']/a").click()
        #这个地方只能用time.sleep
        time.sleep(5)
        driver.find_element_by_id("dateFrom").click()
        driver.find_element_by_id("dateFrom").clear()
        driver.find_element_by_id("dateFrom").send_keys("")
        driver.find_element_by_xpath("//form[@id='orderSearchForm']/div/div[4]").click()
        Select(driver.find_element_by_id("status")).select_by_visible_text(u"手工拣货待定案")
        driver.find_element_by_css_selector("option[value=\"461\"]").click()
        driver.find_element_by_id("orderSearchBtn").click()
        res = driver.find_element_by_xpath(".//*[@id='tra']/td[2]").text
        self.assertEqual('624895985000021',res)
        # driver.find_element_by_xpath("//div[@id='webctx']/table[3]/tbody/tr/td").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [getTable | id=orderListTable.1.1 | ]]
        # for i in range(60):
        #     try:
        #         if "2016-08-31 10:32" == driver.find_element_by_xpath("(//tr[@id='tra']/td[5])[2]").text: break
        #     except: pass
        #     time.sleep(1)
        # else: self.fail("time out")
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | id=orderListTable.1.1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getTable | css=table.dashContainerWhiteBG.0.0 | ]]

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

    '''
    必须内容，unittest tearDown做关闭session，浏览器操作
    '''
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
