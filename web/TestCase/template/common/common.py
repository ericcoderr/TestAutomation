# -*- coding: utf-8 -*-
'''
统一公用方法入口，此入口只是个实例，具体目录根据项目走
'''
class Common:

    @staticmethod
    def login(driver,base_url):
        driver.get(base_url + "/djoms/login")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("oms1059")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("oms1059")
        driver.find_element_by_id("Submit").click()
