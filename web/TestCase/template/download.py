# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import os
import unittest, time, re
from common.common import Common


class Download(unittest.TestCase):
    #如果是selenium ide 录制的脚本，会包含以下代码，可以不管，当QA人员编写TestCase时不写这个方法
    # def setUp(self):
    #     print('old')
    #     #self.driver = webdriver.Firefox()

    def test_download(self):
        driver = self.driver

        #下载操作前文件下载数量
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
        before_download_len = len(os.listdir(self.download_path))
        # driver.get(self.base_url + "/djoms/login")
        # driver.find_element_by_id("userName").clear()
        # driver.find_element_by_id("userName").send_keys("test000")
        # driver.find_element_by_id("userPassword").clear()
        # driver.find_element_by_id("userPassword").send_keys("Aa123456")
        # driver.find_element_by_id("Submit").click()
        Common.login(driver,self.base_url )
        time.sleep(2)
        driver.find_element_by_link_text(u"系统配置").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"PI比例设置").click()
        time.sleep(2)
        driver.find_element_by_id('pIDownExcelModel').click()
        time.sleep(5)
        #self.assertTrue(os.path.exists('d:/20170426092443导入PI比例设置模板.xls'))
        #比较指定下载目录下载后文件数量是否有变化
        after_download_len = len(os.listdir(self.download_path))
        self.assertTrue(after_download_len > before_download_len)

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
