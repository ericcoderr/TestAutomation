import re

from src.common.constant import Field
from src.pages.control import Control
from src.driver import MyDriver
from src.helper.script_helper import Script
from appium.webdriver.common.mobileby import MobileBy
from src.helper.file_names_helper import fileNames
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep


class Expectation(object):

    def __init__(self,case):
        self.case = case
        self.driver = case.driver
        self.control = case.control

    def check(self, *para, **args):
        flag=False
        try:
            exp_hash = para[0]
            value = exp_hash[Field.VALUE]

            if re.match('^\${.*}$', value, flags=0):
                mtd = Script.get_attr(re.sub(r'^\${(.*)}$', r'\1', value))
                flag =mtd(self.case)
                return flag
            elif re.match('\$\$IF_EXIST', value, flags=0):
                try:
                    self.control.find_element(exp_hash[Field.ELEMENT],Expectation.has_ios_name(exp_hash))
                    flag=True
                    return flag
                except BaseException:
                    flag=False
                    return flag
            if Field.ELEMENT in exp_hash:
                element = exp_hash[Field.ELEMENT]
                if MyDriver.is_ios(self.driver):
                    attr_name='name'
                    if Field.EXPECTATION_ATTR in exp_hash:
                        attr_name = exp_hash[Field.EXPECTATION_ATTR]
                    text = self.control.find_element(element,Expectation.has_ios_name(exp_hash)).get_attribute(attr_name)
                else:
                    attr_name='text'
                    if Field.EXPECTATION_ATTR in exp_hash:
                        attr_name = exp_hash[Field.EXPECTATION_ATTR]
                    if attr_name== 'content-desc':
                        text=self.control.find_element_by_located( MobileBy.ACCESSIBILITY_ID, element)
                        if text != None:
                            flag=True
                            return  flag
                    else:
                        text = self.control.find_element(element,False).get_attribute(attr_name)

                if Field.EXPECTATION_MATCHING_TYPE in exp_hash:
                    matching_type = exp_hash[Field.EXPECTATION_MATCHING_TYPE]
                    flag= Expectation.matching(matching_type,text,value)
                    return flag
                else:
                    flag= text.strip() == value.strip()
                    return flag
            else:
                # SET DEFUALT CALSS NAME
                if MyDriver.is_ios(self.driver):
                    class_name = Control.IOS_CLASS_TEXT_VIEW
                    attr_name = Control.IOS_TEXT
                else:
                    class_name = Control.AND_CLASS_TEXT_VIEW
                    attr_name = Control.AND_TEXT

                matching_type=''
                if Field.TYPE in exp_hash:
                    class_name = exp_hash[Field.TYPE]
                if Field.EXPECTATION_MATCHING_TYPE in exp_hash:
                    matching_type = exp_hash[Field.EXPECTATION_MATCHING_TYPE]
                if Field.EXPECTATION_ATTR in exp_hash:
                    attr_name = exp_hash[Field.EXPECTATION_ATTR]

                if matching_type == Field.EXPECTATION_TYPE_TOAST:
                    element = WebDriverWait(self.driver,10,0.7).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='"+value+"']")))
                    if element:
                        return True
                else:
                    elements = self.control.find_elements(class_name)
                    for element in elements:
                        text = element.get_attribute(attr_name)
                        if Expectation.matching(matching_type,text,value):
                            flag = True
                            break
                    return flag
        finally:

            #toast check because start port 8200,sleep 12s
            if 'matching_type' in  locals().keys() and matching_type==Field.EXPECTATION_TYPE_TOAST:
                sleep(12)
            if not flag:
                filename = fileNames()
                image_name = filename.generateImageName(para[1], self.case._testMethodName)
                self.driver.get_screenshot_as_file(image_name)


    @staticmethod
    def matching(_type,text,value):
        if _type == Field.EXPECTATION_MATCHING_TYPE_CONTAINS:
            return value in text
        if _type == Field.EXPECTATION_MATCHING_TYPE_NOT_EQUALS:
            return value != text
        if _type == Field.EXPECTATION_MATCHING_TYPE_NOT_CONTAINS:
            return value not in text
        elif _type == Field.EXPECTATION_REGEX_TYPE:
            return re.match(value, text, flags=0)
        else:
            return value == text

    @staticmethod
    def has_ios_name(exp_hash):
        ios_name=True
        b='True'
        if Field.IOS_NAME in exp_hash:
            ios_name=str(exp_hash[Field.IOS_NAME])==b
        return ios_name


