#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
wait util function
singleton object
'''
from selenium.webdriver.support.ui import WebDriverWait
import threading


class Waiter(object):
    default_time_out = 10
    instance = None
    webDriverWait = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    def __call__(self,driver,element):
        return self.wait(driver,element)

    '''
    singleton
    '''
    @staticmethod
    def getInstance():
        if (Waiter.instance == None):
            Waiter.mutex.acquire()
            if (Waiter.instance == None):
                Waiter.default_time_out = 10
                Waiter.instance = Waiter()
            else:
                Waiter.mutex.release()
        return Waiter.instance


    def wait(self,driver,element):
        return WebDriverWait(driver, Waiter.default_time_out).until(element)

    def implicitly_wait(self, driver):
        driver.implicitly_wait(self.default_time_out)

