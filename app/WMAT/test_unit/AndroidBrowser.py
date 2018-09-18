# -*- coding: UTF-8 -*-
'''
Created on 2016年9月18日
冒烟测试：SMO001:关键字搜索商品
@author: miaoli
'''
import unittest
import sys

sys.path.append('D:\\TestAutomation\\WMAT\\')
import os
import time
import unittest
from appium import webdriver
from src.helper import wait_util
from src.driver import MyDriver
from src.pages.actions import Actions
from src.pages.control import Control
from src.pages.expectation import Expectation
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class AndroidBrowser(unittest.TestCase):
    def setUp(self):
        #android
        desired_caps = {}
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = 'emulator-5554'
        #desired_caps['appPackage'] = 'cn.com.walmart.mobile'
        # desired_caps['appPackage'] = 'com.testerhome.webview'
        # desired_caps['appActivity'] = '.ToastActivity'
        #desired_caps['appActivity'] = '.welcome.WelcomeActivity'
        #desired_caps['autoAcceptAlerts']='true'6
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['app'] = '/Users/eric/Downloads/webview.apk'
        #desired_caps['app'] = 'C:/Users/ehuan12/Desktop/android.apk'
        #desired_caps['url'] = 'http://192.168.21.90:4723/wd/hub'
        #desired_caps['app'] = '/Users/ddxflqm/ownCloud/TIMMY/selendroid-test-app.apk'

        #ios
        #desired_caps = {}
        #desired_caps["unicodeKeyboard"] = "True"
        #desired_caps["resetKeyboard"] = "True"
        #desired_caps['platformName'] = 'ios'
        #desired_caps['platformVersion'] = '9.3'
        #desired_caps['deviceName'] = 'iPhone Simulator'
        #desired_caps['autoAcceptAlerts']='true'
        #desired_caps['app'] = '/Users/ddxflqm/ownCloud/TIMMY/apps/TestApp/build/release-iphonesimulator/TestApp.app'
        #desired_caps['url']='http://192.168.21.80:4723/wd/hub'
        self.driver = webdriver.Remote('http://192.168.21.90:4723/wd/hub',desired_caps)


    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def runTest(self):
        print(self)
        try:
            print('－－－－－－SMO01测试开始：－－－－－－\n')
            # exp_hash = {}
            # exp_hash['value'] = 'www.baidu.com'
            # exp_hash['element'] = 'url'
            # searchPath='//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]'
            # basic_utils.waite_element_by_xpath(self, searchPath).click()
            #self.control = Control(self)
            #self.action = Actions(self)
            #elf.expectation = Expectation(self)
            # element = EC.presence_of_element_located((By.ID, 'com.android.browser:id/url'))
            # element = self.control.find_element('buttonStartWebviewCD')
            # element = self.control.find_element('//UIAApplication[1]/UIAWindow[2]/UIATextField[1]')
            # self.action.disptach_action(element, 'type', 1)
            # element = self.control.find_element('//UIAApplication[1]/UIAWindow[2]/UIATextField[2]')
            # self.action.disptach_action(element, 'type', 2)
            # element = self.control.find_element('ComputeSumButton')
            # self.action.disptach_action('', 'tap', '')
            # self.action.disptach_action('', 'swipe', '126.2,357.4,219,357.4')
            # self.action.disptach_action('', 'wait', '120.2,348.4,110,0')
            # self.driver.desired_capabilities['platformName']
            #self.action.disptach_action('', 'tap', '32,245')
            # self.action.disptach_action('', 'wait', 10)
            #exp_hash = {'value':'','matching':'contains','element':'//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]'}
            #print(self.expectation.check(exp_hash))
            # elements = self.control.find_elements('UIAStaticText')
            # elements[0].get_attribute('label')
            # element = self.control.find_element('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]')
            # self.action.disptach_action(element, 'click', '')
            # element = self.control.find_element( '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.EditText[1]')
            # self.action.disptach_action(element, 'typeEnter', '35')
            # self.driver.activate_ime_engine('com.android.inputmethod.latin/.LatinIME');
            # self.driver.keyevent(7)
            # self.driver.keyevent(67)

            # self.driver.keyevent(66)
            # self.action.disptach_action(element, 'wait',5)
            #element = self.control.find_element('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.Button[1]',False)
            # self.action.disptach_action(element, 'click', '')
            # element = self.control.find_element('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[2]')
            # self.action.disptach_action(element, 'click', '')
            # element = self.control.find_element('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]')
            # self.action.disptach_action(element, 'type', '123')
            # element = self.control.find_element('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.EditText[1]')
            # self.action.disptach_action(element, 'type', '456')

            # waiter = WaitUtil.Waiter.getInstance()
            # node = waiter.wait(self.driver,element)
            # node = basic_utils.waite_element_by_id(self, 'com.android.browser:id/url')
            # node.send_keys('www.baidu.com \n')
            # node.send_keys('www.baidu.com \n')
            # self.action.disptach_action(element, 'swipe','10%,10%,10%,10%')
            # self.action.disptach_action(element, 'switch_to_webview', '')
            # self.driver.switch_to.context('WEBVIEW')

            # input_field = self.control.find_element('name_input')
            # self.action.disptach_action(input_field, 'type', 'Appium User')

            # self.action.disptach_action(element,'swipe','650,40,720,1000')
            # print(self.expectation.check(exp_hash))
            # self.driver
            #self.action.switch_to_app('com.android.settings,.Settings')
            #
            #self.action.background_app(5)
            #self.control.find_element('.contains',False)
            #sleep(5)
            #obj=self.control.find_element('tab_shop_imageview',False)
            #self.driver.start_activity('', '.ToastActivity')

            b= self.driver.find_element(By.ID,'com.testerhome.webview:id/clickToToastActivity')
            print('============')

            b.click()
            time.sleep(2)
            toastButton =self.driver.find_element(By.ID,'com.testerhome.webview:id/toast')
            time.sleep(2)
            #cmd1='adb -s emulator-5554 shell uiautomator events'
            #out=os.popen(cmd1)
            #cmd2='uiautomator events'
            #os.popen(cmd2)
            toastButton.click()
            #print(out)

            #obj=WebDriverWait(self.driver, 10).until( EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "(//*[contains(@text,'Toast Test')]")))
            element = WebDriverWait(self.driver,10,0.7).until(EC.presence_of_element_located((By.XPATH, "//*[@text='Toast Test']")))
            print(element is None)
            if element:
                print(111111)
            time.sleep(15)
            # oo=self.driver.page_source
            # print(oo)
            #obj1=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,".//*[contains(@text,'Toast Test')]")))
            # print(obj1)

        except  BaseException:
            exstr = traceback.format_exc()
            print(exstr)
            print(time.strftime('%Y-%m-%d %H:%M:%S') + 'error')
            result = False
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
